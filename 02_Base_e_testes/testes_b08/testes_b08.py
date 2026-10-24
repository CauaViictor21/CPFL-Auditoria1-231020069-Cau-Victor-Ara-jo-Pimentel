#!/usr/bin/env python3
"""Bloco 08 - testes na base SINTETICA registrada: procedimentos integrais (T1-T4) e amostragem
por unidade monetaria (MUS) com avaliacao pelo limite de Stringer (Poisson, 95%).

REGRA: este codigo le SOMENTE a base registrada e parametros_b08.json. Nao le o gerador,
a pasta RESERVADO_NAO_ABRIR_ATE_CONGELAMENTO, o registro de erros nem gabaritos.
Uso: python testes_b08.py   (caminhos relativos a esta pasta)   Requer: Python 3 + scipy."""
import csv, gzip, hashlib, json, math, os, random, statistics, datetime as dt, collections, time
from scipy.stats import chi2

AQUI = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(AQUI, 'parametros_b08.json'), encoding='utf-8'))
OUT = os.path.join(AQUI, 'saida_b08'); os.makedirs(OUT, exist_ok=True)
t0 = time.time()
pb = os.path.normpath(os.path.join(AQUI, P['base']))
sha = hashlib.sha256(open(pb, 'rb').read()).hexdigest()
assert sha == P['base_sha256_esperado'], 'base diferente da congelada no Bloco 07'

# ---------- leitura (ordem do arquivo = ordem de id_registro) ----------
R = []
with gzip.open(pb, 'rt', encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f):
        r['c'] = int(r['valor_registrado_rs'].replace('.', ''))
        R.append(r)
BV = sum(r['c'] for r in R)
assert all(r['c'] > 0 for r in R), 'ha saldos nulos ou negativos: tratar antes do MUS'
RG = P['regras_teste_100']; vida = RG['vida_util_anos']; db = dt.date(2025, 12, 31)

# ---------- T1 duplicidade ----------
por_bem = collections.defaultdict(list)
for r in R: por_bem[r['id_bem_tecnico']].append(r)
T1 = []; excedente = set()
for bem, lst in por_bem.items():
    if len(lst) > 1:
        lst = sorted(lst, key=lambda x: x['id_registro'])
        iguais = all((x['distribuidora'], x['categoria_cadastrada'], x['data_incorporacao'], x['vnr_base_simulado_rs'],
                      x['fator_atualizacao_simulado'], x['fator_residual_simulado']) ==
                     (lst[0]['distribuidora'], lst[0]['categoria_cadastrada'], lst[0]['data_incorporacao'], lst[0]['vnr_base_simulado_rs'],
                      lst[0]['fator_atualizacao_simulado'], lst[0]['fator_residual_simulado']) for x in lst)
        for x in lst[1:]:
            excedente.add(x['id_registro'])
            T1.append({'id_bem_tecnico': bem, 'id_registro_mantido': lst[0]['id_registro'], 'id_registro_excedente': x['id_registro'],
                       'atributos_identicos': iguais, 'valor_mantido_rs': lst[0]['valor_registrado_rs'],
                       'valor_excedente_rs': x['valor_registrado_rs'], 'distorcao_rs': x['valor_registrado_rs']})
# ---------- T2 baixado com valor ----------
T2 = [{'id_registro': r['id_registro'], 'data_baixa': r['data_baixa'], 'valor_registrado_rs': r['valor_registrado_rs'],
       'distorcao_rs': r['valor_registrado_rs']} for r in R if r['status_cadastral'] == 'BAIXADO' and r['c'] > 0]
baixados = {x['id_registro'] for x in T2}
# ---------- T3 recalculo ----------
razoes = collections.defaultdict(list)
for r in R:
    b = float(r['vnr_base_simulado_rs']) * float(r['fator_atualizacao_simulado']) * float(r['fator_residual_simulado'])
    r['bruto'] = b; razoes[r['distribuidora']].append(r['c'] / 100 / b)
k = {d: statistics.median(v) for d, v in razoes.items()}
T3 = []; esperado = {}
for r in R:
    e = r['bruto'] * k[r['distribuidora']]; esperado[r['id_registro']] = e
    dv = r['c'] / 100 / e - 1
    if abs(dv) > RG['T3_limite']:
        T3.append({'id_registro': r['id_registro'], 'distribuidora': r['distribuidora'], 'valor_registrado_rs': r['valor_registrado_rs'],
                   'valor_recalculado_rs': f'{e:.2f}', 'desvio_pct': round(100 * dv, 3),
                   'distorcao_rs': f"{r['c'] / 100 - e:.2f}", 'sentido': 'SUPERAVALIACAO' if dv > 0 else 'SUBAVALIACAO'})
t3ids = {x['id_registro']: x for x in T3}
# ---------- T4 coerencia residual x idade x vida util da categoria cadastrada ----------
T4 = []
for r in R:
    idade = (db - dt.date.fromisoformat(r['data_incorporacao'])).days / 365.25
    L = vida[r['categoria_cadastrada']]
    esp = round(max(0.01, 1 - idade / L), 4)
    if abs(float(r['fator_residual_simulado']) - esp) > RG['T4_limite']:
        # categoria(s) com a qual o residual seria coerente
        cand = [c for c, Lc in vida.items() if abs(round(max(0.01, 1 - idade / Lc), 4) - float(r['fator_residual_simulado'])) <= RG['T4_limite']]
        T4.append({'id_registro': r['id_registro'], 'categoria_cadastrada': r['categoria_cadastrada'], 'data_incorporacao': r['data_incorporacao'],
                   'residual_registrado': r['fator_residual_simulado'], 'residual_esperado': f'{esp:.4f}',
                   'categoria_coerente_sugerida': ' | '.join(cand) or 'nenhuma', 'efeito_no_saldo_rs': '0.00'})

# ---------- MUS ----------
M = P['mus']; TM = round(M['distorcao_toleravel_rs'] * 100); EM = round(M['distorcao_esperada_rs'] * 100)
beta = M['risco_aceitacao_incorreta']
UL = lambda kk: chi2.ppf(1 - beta, 2 * kk + 2) / 2   # limite superior de Poisson para kk erros
RF0 = UL(0)
n = math.ceil(BV * RF0 / (TM - EM * M['fator_expansao']))
J = BV / n
rng = random.Random(M['semente_ponto_inicial']); inicio = rng.uniform(0, J)
pontos = [inicio + i * J for i in range(n)]
amostra = []; acum = 0; ip = 0; integrais = []
for r in R:
    ini, fim = acum, acum + r['c']; hits = 0
    while ip < n and pontos[ip] < fim:
        hits += 1; ip += 1
    if r['c'] >= J: integrais.append(r['id_registro'])
    if hits:
        amostra.append((r, ini, hits))
    acum = fim
assert ip == n
linhas = []; taints = []
for ordem, (r, ini, hits) in enumerate(amostra, 1):
    rid = r['id_registro']; book = r['c'] / 100; obs = []
    aud = book
    if rid in baixados: aud = 0.0; obs.append('T2 BAIXADO com valor')
    elif rid in excedente: aud = 0.0; obs.append('T1 registro excedente de bem duplicado')
    elif rid in t3ids: aud = round(esperado[rid], 2); obs.append('T3 recalculo diverge ' + str(t3ids[rid]['desvio_pct']) + '%')
    if any(x['id_registro'] == rid for x in T4): obs.append('T4 residual incoerente com a categoria (sem efeito monetario)')
    dist = round(book - aud, 2); taint = dist / book if book else 0
    if dist != 0: taints.append(taint)
    linhas.append({'ordem': ordem, 'id_registro': rid, 'distribuidora': r['distribuidora'], 'categoria_cadastrada': r['categoria_cadastrada'],
                   'valor_registrado_rs': f'{book:.2f}', 'acumulado_inicio_rs': f'{ini / 100:.2f}', 'selecoes': hits,
                   'valor_auditado_simulado_rs': f'{aud:.2f}', 'distorcao_rs': f'{dist:.2f}', 'taint': round(taint, 6),
                   'distorcao_projetada_rs': f'{taint * J / 100:.2f}', 'resultado': '; '.join(obs) or 'Sem excecao'})
over = sorted([t for t in taints if t > 0], reverse=True); under = sorted([t for t in taints if t < 0])
bp = J * RF0 / 100
incr = [t * (J / 100) * (UL(i + 1) - UL(i)) for i, t in enumerate(over)]
proj_over = sum(t * J / 100 for t in over); proj_under = sum(t * J / 100 for t in under)
uml = bp + sum(incr)
mus = {'populacao_rs': BV / 100, 'unidades_amostrais_itens': len(R), 'risco_aceitacao_incorreta': beta,
       'fator_confianca_0_erros': round(RF0, 4), 'distorcao_toleravel_rs': TM / 100, 'distorcao_esperada_rs': EM / 100,
       'fator_expansao': M['fator_expansao'], 'tamanho_amostra_n': n, 'intervalo_amostral_rs': round(J / 100, 2),
       'ponto_inicial_rs': round(inicio / 100, 2), 'semente': M['semente_ponto_inicial'], 'itens_distintos_selecionados': len(amostra),
       'itens_selecionados_mais_de_uma_vez': sum(1 for a in amostra if a[2] > 1), 'itens_selecao_integral_(>=J)': integrais,
       'distorcoes_superavaliacao_na_amostra': len(over), 'distorcoes_subavaliacao_na_amostra': len(under),
       'soma_distorcoes_amostra_rs': round(sum(float(l['distorcao_rs']) for l in linhas), 2),
       'distorcao_projetada_superavaliacao_rs': round(proj_over, 2), 'distorcao_projetada_subavaliacao_rs': round(proj_under, 2),
       'precisao_basica_rs': round(bp, 2), 'incrementos_precisao_rs': [round(x, 2) for x in incr],
       'limite_superior_distorcao_UML_rs': round(uml, 2),
       'conclusao_regra': 'UML <= distorcao toleravel' if uml <= TM / 100 else 'UML > distorcao toleravel: ampliar procedimentos'}

def dump(nome, rows):
    p = os.path.join(OUT, nome)
    with open(p, 'w', newline='', encoding='utf-8') as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n'); w.writeheader(); w.writerows(rows)
    return p
arqs = [dump('T1_duplicidades.csv', T1), dump('T2_baixados_com_valor.csv', T2), dump('T3_recalculo_divergente.csv', T3),
        dump('T4_residual_incoerente.csv', T4), dump('MUS_amostra_resultados.csv', linhas)]
s = lambda rows, k: round(sum(float(x[k]) for x in rows), 2)
res = {'executado_em': dt.datetime.now().isoformat(timespec='seconds'), 'duracao_s': round(time.time() - t0, 1),
       'base_sha256': sha, 'linhas': len(R), 'total_rs': BV / 100, 'k_estimado_por_distribuidora': {d: round(v, 8) for d, v in k.items()},
       'T1': {'pares': len(T1), 'atributos_identicos': sum(1 for x in T1 if x['atributos_identicos']), 'distorcao_rs': s(T1, 'distorcao_rs')},
       'T2': {'itens': len(T2), 'distorcao_rs': s(T2, 'distorcao_rs')},
       'T3': {'itens': len(T3), 'superavaliacao_itens': sum(1 for x in T3 if x['sentido'] == 'SUPERAVALIACAO'),
              'superavaliacao_rs': round(sum(float(x['distorcao_rs']) for x in T3 if x['sentido'] == 'SUPERAVALIACAO'), 2),
              'subavaliacao_itens': sum(1 for x in T3 if x['sentido'] == 'SUBAVALIACAO'),
              'subavaliacao_rs': round(sum(float(x['distorcao_rs']) for x in T3 if x['sentido'] == 'SUBAVALIACAO'), 2),
              'sobreposicao_com_T1_T2': sum(1 for x in T3 if x['id_registro'] in excedente or x['id_registro'] in baixados)},
       'T4': {'itens': len(T4), 'sobreposicao_com_T3': sum(1 for x in T4 if x['id_registro'] in t3ids)},
       'MUS': mus}
res['distorcao_conhecida_liquida_rs'] = round(res['T1']['distorcao_rs'] + res['T2']['distorcao_rs'] + res['T3']['superavaliacao_rs'] + res['T3']['subavaliacao_rs'], 2)
pj = os.path.join(OUT, 'resultados_b08.json'); json.dump(res, open(pj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))

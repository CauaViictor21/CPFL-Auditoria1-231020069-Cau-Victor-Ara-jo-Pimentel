#!/usr/bin/env python3
"""Bloco 08 - resposta ao resultado do MUS (NBC TA 530 itens 12, 14, 15; NBC TA 450 item 6),
definida DEPOIS da execucao de testes_b08.py e ANTES da abertura dos arquivos reservados.

Logica:
 1. As 6 distorcoes da amostra pertencem a classes identificadas integralmente por T1, T2 e T3
    (nao sao anomalias). A distorcao dessas classes e CONHECIDA (100%), nao projetada.
 2. A populacao residual exclui os registros sinalizados por T1 (excedentes), T2 e T3.
 3. Ampliacao: nova amostra MUS, independente (nova semente), sobre a populacao residual, com
    tamanho tal que superavaliacao conhecida bruta + precisao basica <= distorcao toleravel.
 4. Avaliacao: superavaliacao conhecida + UML residual comparados com a distorcao toleravel.
Le SOMENTE a base registrada, parametros_b08.json e saida_b08/. Requer scipy."""
import csv, gzip, json, math, os, random, datetime as dt
from scipy.stats import chi2

AQUI = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(AQUI, 'saida_b08')
P = json.load(open(os.path.join(AQUI, 'parametros_b08.json'), encoding='utf-8'))
res = json.load(open(os.path.join(S, 'resultados_b08.json'), encoding='utf-8'))
ids = lambda f, k: {r[k] for r in csv.DictReader(open(os.path.join(S, f), encoding='utf-8'))}
flag = ids('T1_duplicidades.csv', 'id_registro_excedente') | ids('T2_baixados_com_valor.csv', 'id_registro') | ids('T3_recalculo_divergente.csv', 'id_registro')
beta = P['mus']['risco_aceitacao_incorreta']; UL = lambda k: chi2.ppf(1 - beta, 2 * k + 2) / 2
DT = P['mus']['distorcao_toleravel_rs']
sup_conhecida = res['T1']['distorcao_rs'] + res['T2']['distorcao_rs'] + res['T3']['superavaliacao_rs']
sub_conhecida = res['T3']['subavaliacao_rs']
R = []
with gzip.open(os.path.normpath(os.path.join(AQUI, P['base'])), 'rt', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r['id_registro'] not in flag: R.append((r['id_registro'], int(r['valor_registrado_rs'].replace('.', ''))))
BVr = sum(c for _, c in R) / 100
folga = DT - sup_conhecida                      # espaco para distorcao nao detectada
J2 = folga / UL(0); n2 = math.ceil(BVr / J2); J2 = BVr / n2
rng = random.Random(P['mus']['semente_ponto_inicial'] + 1); ini = rng.uniform(0, J2 * 100)
pts = [ini + i * J2 * 100 for i in range(n2)]; ip = 0; acum = 0; sel = []
for rid, c in R:
    h = 0
    while ip < n2 and pts[ip] < acum + c: h += 1; ip += 1
    if h: sel.append((rid, c, acum, h))
    acum += c
# itens sorteados ja passaram por T1-T4; na simulacao o "valor auditado" = registrado se nao sinalizado
t4 = ids('T4_residual_incoerente.csv', 'id_registro')
linhas = [{'ordem': i, 'id_registro': rid, 'valor_registrado_rs': f'{c / 100:.2f}', 'acumulado_inicio_rs': f'{a / 100:.2f}',
           'selecoes': h, 'valor_auditado_simulado_rs': f'{c / 100:.2f}', 'distorcao_rs': '0.00',
           'observacao': 'T4: categoria incoerente (sem efeito monetario)' if rid in t4 else 'Sem excecao'}
          for i, (rid, c, a, h) in enumerate(sel, 1)]
with open(os.path.join(S, 'MUS_ampliacao_residual.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator='\n'); w.writeheader(); w.writerows(linhas)
uml2 = UL(0) * J2  # zero distorcoes na amostra residual
out = {'executado_em': dt.datetime.now().isoformat(timespec='seconds'),
       'etapa_1_desenho_original': {'UML_rs': res['MUS']['limite_superior_distorcao_UML_rs'], 'DT_rs': DT, 'resultado': 'UML > DT'},
       'etapa_2_natureza_causa': 'As 6 distorcoes da amostra pertencem as classes T1/T2/T3, identificadas em 100% da populacao; sistematicas, nao anomalias (530 item 13 nao aplicavel)',
       'superavaliacao_conhecida_rs': round(sup_conhecida, 2), 'subavaliacao_conhecida_rs': round(sub_conhecida, 2),
       'distorcao_conhecida_liquida_rs': round(sup_conhecida + sub_conhecida, 2),
       'registros_sinalizados_excluidos': len(flag), 'populacao_residual_rs': round(BVr, 2), 'populacao_residual_itens': len(R),
       'folga_para_nao_detectado_rs': round(folga, 2), 'ampliacao_n': n2, 'ampliacao_intervalo_rs': round(J2, 2),
       'ampliacao_semente': P['mus']['semente_ponto_inicial'] + 1, 'ampliacao_itens_distintos': len(sel),
       'ampliacao_distorcoes': 0, 'ampliacao_itens_T4': sum(1 for l in linhas if l['observacao'] != 'Sem excecao'),
       'UML_residual_rs': round(uml2, 2),
       'superavaliacao_conhecida_mais_UML_residual_rs': round(sup_conhecida + uml2, 2),
       'conclusao': 'superavaliacao conhecida + UML residual <= DT' if sup_conhecida + uml2 <= DT + 0.01 else 'excede DT',
       'limite_didatico': 'Na simulacao, o procedimento aplicado aos itens sorteados reutiliza as regras T1-T4; a amostra nao pode revelar tipos de erro nao programados nos testes.'}
json.dump(out, open(os.path.join(S, 'avaliacao_complementar_b08.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

#!/usr/bin/env python3
"""Verificacoes de integridade da base SINTETICA registrada (Bloco 07).
Le SOMENTE a base registrada e o config; nao le a pasta RESERVADO_NAO_ABRIR_ATE_CONGELAMENTO.
Uso: python verificar_base_cpfl_v2.py   (caminhos relativos a esta pasta)
Saida: saida/CPFL_SINTETICA_verificacoes.json"""
import csv, gzip, json, os, re, statistics, datetime as dt, collections, hashlib, time

AQUI = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(AQUI, 'config_base_cpfl_v2.json'), encoding='utf-8'))
pb = os.path.join(AQUI, cfg['saidas']['base_registrada'])
t0 = time.time()
CAB = ['id_registro', 'id_bem_tecnico', 'distribuidora', 'categoria_cadastrada', 'data_incorporacao',
       'vnr_base_simulado_rs', 'fator_atualizacao_simulado', 'fator_residual_simulado', 'status_cadastral',
       'data_baixa', 'valor_registrado_rs', 'data_base', 'origem_dados']
cats = cfg['categorias']; dists = list(cfg['saldos_publicados_rs_mil'])
falhas = collections.Counter(); ex_falha = collections.defaultdict(list)
def falha(cod, rid):
    falhas[cod] += 1
    if len(ex_falha[cod]) < 5: ex_falha[cod].append(rid)
n = 0; ids = set(); bens = collections.Counter(); vazios = collections.Counter()
soma_d = collections.Counter(); soma_dc = collections.Counter(); qtd_dc = collections.Counter()
status = collections.Counter(); anos = collections.Counter(); razoes = collections.defaultdict(list)
dec2 = re.compile(r'^\d+\.\d{2}$'); dec4 = re.compile(r'^\d+\.\d{4}$')
with gzip.open(pb, 'rt', encoding='utf-8', newline='') as f:
    rd = csv.reader(f); cab = next(rd)
    cab_ok = cab == CAB
    for r in rd:
        n += 1
        if len(r) != 13: falha('F01 colunas != 13', r[0] if r else n); continue
        rid, bem, di, cat, dinc, vnr, fat, res, st, dbx, val, dbase, orig = r
        for k, v in zip(CAB, r):
            if v == '': vazios[k] += 1
        if rid in ids: falha('F02 id_registro repetido', rid)
        ids.add(rid); bens[bem] += 1
        if not re.fullmatch(r'AFC-SIM-\d{7}', rid): falha('F03 formato id_registro', rid)
        if not re.fullmatch(r'BEM-SIM-\d{7}', bem): falha('F04 formato id_bem_tecnico', rid)
        if di not in dists: falha('F05 distribuidora fora do dominio', rid)
        if cat not in cats: falha('F06 categoria fora do dominio', rid)
        try:
            d = dt.date.fromisoformat(dinc)
            if not (cfg['ano_minimo_incorporacao'] <= d.year <= 2025): falha('F07 data fora do periodo', rid)
            anos[d.year] += 1
        except ValueError: falha('F08 data invalida', rid)
        if not (dec2.match(vnr) and dec2.match(val) and dec4.match(fat) and dec4.match(res)):
            falha('F09 formato numerico/precisao', rid); continue
        v_c = int(val.replace('.', ''))
        if v_c <= 0: falha('F10 valor <= 0', rid)
        if not (1.0 <= float(fat) <= 1.30): falha('F11 fator atualizacao fora do intervalo', rid)
        if not (0.01 <= float(res) <= 1.0): falha('F12 fator residual fora do intervalo', rid)
        if st not in ('ATIVO', 'BAIXADO'): falha('F13 status fora do dominio', rid)
        if st == 'ATIVO' and dbx: falha('F14 ATIVO com data de baixa', rid)
        if st == 'BAIXADO':
            try: dt.date.fromisoformat(dbx)
            except ValueError: falha('F15 BAIXADO sem data de baixa valida', rid)
        if dbase != cfg['data_base'] or orig != 'SINTETICO': falha('F16 data_base/origem invalida', rid)
        status[st] += 1; soma_d[di] += v_c; soma_dc[(di, cat)] += v_c; qtd_dc[(di, cat)] += 1
        # consistencia economica agregada: valor / (VNR x fator x residual) por distribuidora
        bruto = float(vnr) * float(fat) * float(res)
        if bruto > 0 and len(razoes[di]) < 50000: razoes[di].append(v_c / 100 / bruto)
alvo = {k: v['saldo'] * 100000 for k, v in cfg['saldos_publicados_rs_mil'].items()}
cons = cfg['saldo_consolidado_rs_mil']['saldo'] * 100000
rep = {k: v for k, v in bens.items() if v > 1}
res = {
    'arquivo': os.path.relpath(pb, AQUI), 'sha256': hashlib.sha256(open(pb, 'rb').read()).hexdigest(),
    'bytes': os.path.getsize(pb), 'executado_em': dt.datetime.now().isoformat(timespec='seconds'),
    'duracao_s': round(time.time() - t0, 1),
    'cabecalho_confere': cab_ok, 'linhas_dados': n, 'ids_registro_unicos': len(ids),
    'ids_bem_tecnico_distintos': len(bens),
    'ids_bem_tecnico_repetidos': len(rep), 'linhas_excedentes_por_bem_repetido': sum(v - 1 for v in rep.values()),
    'max_ocorrencias_mesmo_bem': max(bens.values()),
    'status': dict(status), 'campos_vazios': dict(vazios),
    'falhas_de_geracao': dict(falhas), 'exemplos_falhas': dict(ex_falha),
    'total_rs': sum(soma_d.values()) / 100, 'saldo_publicado_rs': cons / 100,
    'diferenca_total_rs': (sum(soma_d.values()) - cons) / 100,
    'por_distribuidora': {d: {'total_rs': soma_d[d] / 100, 'saldo_publicado_rs': alvo[d] / 100,
                              'diferenca_rs': (soma_d[d] - alvo[d]) / 100,
                              'linhas': sum(q for (dd, c), q in qtd_dc.items() if dd == d)} for d in dists},
    'por_distribuidora_categoria': [{'distribuidora': d, 'categoria': c, 'linhas': qtd_dc[(d, c)],
                                     'total_rs': soma_dc[(d, c)] / 100} for d in dists for c in cats],
    'mediana_valor_sobre_vnr_fator_residual': {d: round(statistics.median(v), 6) for d, v in razoes.items()},
    'fator_escala_publicado_no_resumo': json.load(open(os.path.join(AQUI, cfg['saidas']['resumo_execucao']), encoding='utf-8'))['fator_escala_por_distribuidora'],
    'incorporacoes_por_ano': dict(sorted(anos.items())),
}
out = os.path.join(AQUI, 'saida', 'CPFL_SINTETICA_verificacoes.json')
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('por_distribuidora_categoria', 'incorporacoes_por_ano')}, ensure_ascii=False, indent=1))

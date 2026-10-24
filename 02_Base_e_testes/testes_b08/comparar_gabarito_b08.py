#!/usr/bin/env python3
"""Bloco 08 - comparacao POSTERIOR ao congelamento (B08_congelamento.json registrado no Drive em
23/10/2026 19:55:53 -03). Le os arquivos reservados gerados pelo gerador v2, confere seus hashes
com os congelados no Bloco 07 e mede deteccoes, omissoes e falsos positivos."""
import csv, gzip, hashlib, json, os, collections

AQUI = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(AQUI, 'saida_b08')
RES = os.path.normpath(os.path.join(AQUI, '..', 'base_v2', 'RESERVADO_NAO_ABRIR_ATE_CONGELAMENTO'))
cong = json.load(open(os.path.join(AQUI, 'B08_congelamento.json'), encoding='utf-8'))
arq = {'referencia': 'CPFL_SINTETICA_Base_referencia_sem_erros.csv.gz', 'registro_erros': 'CPFL_SINTETICA_Registro_erros_inseridos.csv',
       'ponte': 'CPFL_SINTETICA_Ponte_efeito_erros.json'}
hashes_ok = {k: hashlib.sha256(open(os.path.join(RES, v), 'rb').read()).hexdigest() == cong['reservados_sha256_esperados'][k] for k, v in arq.items()}
for f in cong['arquivos_sha256']:  # saidas dos testes nao foram alteradas apos o congelamento
    assert hashlib.sha256(open(os.path.join(AQUI, f), 'rb').read()).hexdigest() == cong['arquivos_sha256'][f], f
ponte = json.load(open(os.path.join(RES, arq['ponte']), encoding='utf-8'))
G = list(csv.DictReader(open(os.path.join(RES, arq['registro_erros']), encoding='utf-8')))
gt = collections.defaultdict(set); ef = collections.defaultdict(float); orig = {}
for g in G:
    gt[g['tipo_erro']].add(g['id_registro']); ef[g['id_registro']] = float(g['efeito_no_saldo_rs'])
    if g['tipo_erro'] == 'DUPLICIDADE_CADASTRAL': orig[g['id_registro']] = g['id_registro_bem_original']
rd = lambda f: list(csv.DictReader(open(os.path.join(S, f), encoding='utf-8')))
T1, T2, T3, T4 = rd('T1_duplicidades.csv'), rd('T2_baixados_com_valor.csv'), rd('T3_recalculo_divergente.csv'), rd('T4_residual_incoerente.csv')
def m(det, verdade):
    det, verdade = set(det), set(verdade)
    return {'sinalizados': len(det), 'verdadeiros': len(verdade), 'detectados': len(det & verdade),
            'omitidos': len(verdade - det), 'falsos_positivos': len(det - verdade),
            'taxa_deteccao': round(len(det & verdade) / len(verdade), 4) if verdade else None}
# T1 em nivel de PAR (o teste nao sabe qual dos dois e o original; convencao = id maior)
par_det = {frozenset((x['id_registro_mantido'], x['id_registro_excedente'])) for x in T1}
par_ver = {frozenset((d, orig[d])) for d in gt['DUPLICIDADE_CADASTRAL']}
t1_conv = m([x['id_registro_excedente'] for x in T1], gt['DUPLICIDADE_CADASTRAL'])
out = {'hashes_reservados_conferem': hashes_ok, 'saidas_inalteradas_desde_congelamento': True,
       'T1_pares': {'sinalizados': len(par_det), 'verdadeiros': len(par_ver), 'detectados': len(par_det & par_ver),
                    'omitidos': len(par_ver - par_det), 'falsos_positivos': len(par_det - par_ver)},
       'T1_convencao_id_maior_acertou_o_excedente': t1_conv['detectados'],
       'T2': m([x['id_registro'] for x in T2], gt['BAIXADO_MANTIDO']),
       'T3_super': m([x['id_registro'] for x in T3 if x['sentido'] == 'SUPERAVALIACAO'], gt['SUPERAVALIACAO']),
       'T3_sub': m([x['id_registro'] for x in T3 if x['sentido'] == 'SUBAVALIACAO'], gt['SUBAVALIACAO']),
       'T4_classificacao': m([x['id_registro'] for x in T4], gt['CLASSIFICACAO_INCORRETA'])}
# efeito monetario: estimado pelos testes x verdadeiro
est = {'DUPLICIDADE_CADASTRAL': sum(float(x['distorcao_rs']) for x in T1), 'BAIXADO_MANTIDO': sum(float(x['distorcao_rs']) for x in T2),
       'SUPERAVALIACAO': sum(float(x['distorcao_rs']) for x in T3 if x['sentido'] == 'SUPERAVALIACAO'),
       'SUBAVALIACAO': sum(float(x['distorcao_rs']) for x in T3 if x['sentido'] == 'SUBAVALIACAO'), 'CLASSIFICACAO_INCORRETA': 0.0}
out['efeito_monetario_por_tipo'] = {t: {'estimado_testes_rs': round(est[t], 2), 'verdadeiro_rs': ponte['efeito_por_tipo_rs'][t],
                                        'diferenca_rs': round(est[t] - ponte['efeito_por_tipo_rs'][t], 2)} for t in est}
out['ponte'] = ponte
out['distorcao_conhecida_liquida_testes_rs'] = round(sum(est.values()), 2)
r = json.load(open(os.path.join(S, 'resultados_b08.json'), encoding='utf-8'))['MUS']
c = json.load(open(os.path.join(S, 'avaliacao_complementar_b08.json'), encoding='utf-8'))
sup_ver = sum(v for t, v in ponte['efeito_por_tipo_rs'].items() if v > 0)
out['MUS_vs_verdade'] = {'superavaliacao_verdadeira_bruta_rs': round(sup_ver, 2),
                         'projecao_superavaliacao_desenho_original_rs': r['distorcao_projetada_superavaliacao_rs'],
                         'erro_da_projecao_rs': round(r['distorcao_projetada_superavaliacao_rs'] - sup_ver, 2),
                         'UML_desenho_original_rs': r['limite_superior_distorcao_UML_rs'],
                         'UML_cobre_a_verdade': r['limite_superior_distorcao_UML_rs'] >= sup_ver,
                         'conhecida_mais_UML_residual_rs': c['superavaliacao_conhecida_mais_UML_residual_rs'],
                         'cobre_a_verdade': c['superavaliacao_conhecida_mais_UML_residual_rs'] >= sup_ver}
# itens da amostra: tipo verdadeiro
am = rd('MUS_amostra_resultados.csv'); tipo = {i: t for t, s in gt.items() for i in s}
out['amostra_MUS_itens_com_erro_verdadeiro'] = collections.Counter(tipo.get(x['id_registro'], 'sem erro') for x in am)
out['amostra_MUS_itens_com_erro_verdadeiro'] = dict(out['amostra_MUS_itens_com_erro_verdadeiro'])
am2 = rd('MUS_ampliacao_residual.csv')
out['ampliacao_itens_com_erro_verdadeiro'] = dict(collections.Counter(tipo.get(x['id_registro'], 'sem erro') for x in am2))
# omissoes de T4: detalhar
omit4 = gt['CLASSIFICACAO_INCORRETA'] - {x['id_registro'] for x in T4}
out['T4_omitidos_ids'] = sorted(omit4)
json.dump(out, open(os.path.join(S, 'comparacao_gabarito_b08.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items()}, ensure_ascii=False, indent=1))

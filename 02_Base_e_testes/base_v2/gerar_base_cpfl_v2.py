#!/usr/bin/env python3
"""Gerador da base SINTETICA do ativo financeiro da concessao (CPFL Energia, 2025) - versao 2.

Trabalho academico (UnB, Auditoria 1, matricula 231020069). Nenhuma linha representa
dado interno da CPFL Energia S.A.; apenas os saldos publicados por distribuidora sao reais
(ver config). Dependencias: somente a biblioteca padrao do Python 3 (>= 3.8).

Uso:  python gerar_base_cpfl_v2.py [config.json] [--previa N]
Todos os caminhos sao relativos a pasta deste script.

Logica (resumo):
 1. Cada linha = uma unidade cadastral de infraestrutura de distribuicao cujo valor residual
    compoe o direito de indenizacao (nota 11). Valor = VNR base x fator de atualizacao x fator
    residual x fator de escala da distribuidora.
 2. Fator residual = 1 - idade/vida util da categoria (dependencia economica).
 3. Cenario de referencia (sem erros): 500.000 bens.
 4. Cenario registrado (com erros): referencia + 5 tipos de erro (1.000 cada); duplicidades
    sao 1.000 linhas adicionais -> 501.000 linhas.
 5. Escala: um unico fator por distribuidora, aplicado antes do arredondamento a TODAS as linhas
    do cenario registrado, para que o total registrado de cada distribuidora iguale o saldo
    publicado (a populacao deve conciliar com o razao). Arredondamento por maior resto (centavos).
 6. Valor correto de cada registro e efeito do erro sao gravados em pasta reservada; o efeito
    total e a ponte saldo publicado -> saldo de referencia ficam explicitos (sem ajuste oculto).
"""
import csv, datetime as dt, gzip, hashlib, json, os, platform, random, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
def caminho(rel): return os.path.join(AQUI, rel)

def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def maior_resto(valores, alvo_centavos):
    """Converte valores (float, centavos) em inteiros que somam exatamente alvo_centavos."""
    base = [int(v) for v in valores]
    falta = alvo_centavos - sum(base)
    ordem = sorted(range(len(valores)), key=lambda i: (valores[i] - base[i]), reverse=True)
    if falta < 0 or falta > len(valores):
        raise ValueError('diferenca de arredondamento fora do esperado')
    for i in ordem[:falta]: base[i] += 1
    return base

def main():
    args = [a for a in sys.argv[1:]]
    previa = None
    if '--previa' in args:
        k = args.index('--previa'); previa = int(args[k + 1]); del args[k:k + 2]
    cfg_path = caminho(args[0]) if args else caminho('config_base_cpfl_v2.json')
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    t0 = time.time()
    rng = random.Random(cfg['semente'])
    N = cfg['linhas_referencia']
    data_base = dt.date.fromisoformat(cfg['data_base'])
    cats = cfg['categorias']; catn = list(cats)
    alvo = {k: v['saldo'] * 1000 * 100 for k, v in cfg['saldos_publicados_rs_mil'].items()}  # centavos
    cons = cfg['saldo_consolidado_rs_mil']['saldo'] * 1000 * 100
    assert sum(alvo.values()) == cons, 'saldos por distribuidora nao somam o consolidado'

    # 1) linhas por distribuidora proporcionais ao saldo publicado (maior resto)
    empresas = list(alvo)
    cotas = maior_resto([N * alvo[e] / cons for e in empresas], N)
    dist = []
    for e, q in zip(empresas, cotas): dist += [e] * q
    rng.shuffle(dist)

    # 2) cenario de referencia
    ref = []
    for i in range(N):
        cat = rng.choices(catn, [cats[c]['peso'] for c in catn])[0]
        vida = cats[cat]['vida_util_anos']
        ano0 = max(cfg['ano_minimo_incorporacao'], data_base.year - vida + 1)
        d = dt.date(rng.randint(ano0, data_base.year), rng.randint(1, 12), rng.randint(1, 28))
        idade = (data_base - d).days / 365.25
        resid = round(max(0.0100, 1 - idade / vida), 4)
        vnr = round(cats[cat]['vnr_base_unitario_rs'] * rng.uniform(*cfg['dispersao_vnr_unitario']), 2)
        fat = round(rng.uniform(*cfg['fator_atualizacao_intervalo']), 4)
        ref.append({'bem': f'BEM-SIM-{i + 1:07d}', 'dist': dist[i], 'cat': cat, 'data': d.isoformat(),
                    'vnr': vnr, 'fat': fat, 'resid': resid, 'status': 'ATIVO', 'data_baixa': '',
                    'bruto': vnr * fat * resid})

    # 3) erros (registros distintos; duplicidades copiam bens nao afetados por outros erros)
    E = cfg['erros']; ne = E['por_tipo']; tipos = E['tipos']
    tipos_valor = [t for t in tipos if t != 'DUPLICIDADE_CADASTRAL']
    escolhidos = rng.sample(range(N), ne * len(tipos_valor))
    erro = {}
    for j, idx in enumerate(escolhidos): erro[idx] = tipos_valor[j // ne]
    reg = []  # cenario registrado: campos registrados + verdade
    for i, r in enumerate(ref):
        x = dict(r); x['tipo'] = erro.get(i, ''); x['bruto_correto'] = r['bruto']
        t = x['tipo']
        if t == 'SUPERAVALIACAO':
            x['bruto'] = r['bruto'] * (1 + rng.uniform(*E['intervalo_super_sub']))
        elif t == 'SUBAVALIACAO':
            x['bruto'] = r['bruto'] * (1 - rng.uniform(*E['intervalo_super_sub']))
        elif t == 'BAIXADO_MANTIDO':
            x['status'] = 'BAIXADO'
            x['data_baixa'] = dt.date(data_base.year, rng.randint(1, 12), rng.randint(1, 28)).isoformat()
            x['bruto_correto'] = 0.0
        elif t == 'CLASSIFICACAO_INCORRETA':
            x['cat_correta'] = r['cat']
            x['cat'] = rng.choice([c for c in catn if c != r['cat']])
        reg.append(x)
    # duplicidades: 1.000 linhas ADICIONAIS que copiam bens nao afetados por outros erros
    limpos = [i for i in range(N) if i not in erro]
    fontes = rng.sample(limpos, ne)
    for f in fontes:
        x = dict(ref[f]); x['tipo'] = 'DUPLICIDADE_CADASTRAL'
        x['bruto_correto'] = 0.0
        reg.append(x)

    # 4) escala por distribuidora e centavos exatos
    fatores = {}
    for e in empresas:
        idx = [k for k, x in enumerate(reg) if x['dist'] == e]
        s = sum(reg[k]['bruto'] for k in idx)
        fatores[e] = alvo[e] / (s * 100)
        cent = maior_resto([reg[k]['bruto'] * 100 * fatores[e] for k in idx], alvo[e])
        for k, c in zip(idx, cent):
            x = reg[k]; x['valor_c'] = c
            if x['tipo'] in ('', 'CLASSIFICACAO_INCORRETA'):
                x['correto_c'] = c
            else:
                x['correto_c'] = round(x['bruto_correto'] * 100 * fatores[e])

    # 5) embaralhar e numerar registros (o ID nao revela origem nem erro)
    ordem = list(range(len(reg))); rng.shuffle(ordem)
    reg = [reg[k] for k in ordem]
    for n, x in enumerate(reg, 1): x['id'] = f'AFC-SIM-{n:07d}'

    cab = ['id_registro', 'id_bem_tecnico', 'distribuidora', 'categoria_cadastrada', 'data_incorporacao',
           'vnr_base_simulado_rs', 'fator_atualizacao_simulado', 'fator_residual_simulado', 'status_cadastral',
           'data_baixa', 'valor_registrado_rs', 'data_base', 'origem_dados']
    def linha(x):
        return [x['id'], x['bem'], x['dist'], x['cat'], x['data'], f"{x['vnr']:.2f}", f"{x['fat']:.4f}",
                f"{x['resid']:.4f}", x['status'], x['data_baixa'], f"{x['valor_c'] // 100}.{x['valor_c'] % 100:02d}",
                cfg['data_base'], 'SINTETICO']

    if previa:
        w = csv.writer(sys.stdout); w.writerow(cab)
        for x in reg[:previa]: w.writerow(linha(x))
        return

    S = cfg['saidas']
    os.makedirs(caminho('saida'), exist_ok=True)
    resv = caminho(S['reservado_dir']); os.makedirs(resv, exist_ok=True)
    pb = caminho(S['base_registrada'])
    with gzip.GzipFile(pb, 'wb', mtime=0) as gz:  # mtime=0 -> mesmo arquivo a cada execucao
        txt = __import__('io').TextIOWrapper(gz, encoding='utf-8', newline='')
        w = csv.writer(txt, lineterminator='\n'); w.writerow(cab)
        for x in reg: w.writerow(linha(x))
        txt.flush(); txt.detach()

    # reservados: referencia, registro de erros, ponte (NAO consultar antes do congelamento dos testes)
    pr = os.path.join(resv, S['referencia'])
    with gzip.GzipFile(pr, 'wb', mtime=0) as gz:
        txt = __import__('io').TextIOWrapper(gz, encoding='utf-8', newline='')
        w = csv.writer(txt, lineterminator='\n')
        w.writerow(['id_registro', 'id_bem_tecnico', 'distribuidora', 'categoria_correta', 'status_correto', 'valor_correto_rs'])
        for x in reg:
            cat = x.get('cat_correta', x['cat']) if x['tipo'] == 'CLASSIFICACAO_INCORRETA' else x['cat']
            st = 'ATIVO' if x['tipo'] != 'BAIXADO_MANTIDO' else 'BAIXADO'
            if x['tipo'] == 'DUPLICIDADE_CADASTRAL': st = 'INEXISTENTE (duplicidade)'
            w.writerow([x['id'], x['bem'], x['dist'], cat, st, f"{x['correto_c'] / 100:.2f}"])
        txt.flush(); txt.detach()
    pe = os.path.join(resv, S['registro_erros'])
    efeito = {t: 0 for t in tipos}; qt = {t: 0 for t in tipos}
    with open(pe, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['id_registro', 'tipo_erro', 'campo_alterado', 'conteudo_correto', 'conteudo_registrado',
                    'valor_correto_rs', 'valor_registrado_rs', 'efeito_no_saldo_rs', 'id_registro_bem_original'])
        orig_id = {}
        for x in reg:
            if x['tipo'] == '' and x['bem'] not in orig_id: orig_id[x['bem']] = x['id']
        for x in reg:
            t = x['tipo']
            if not t: continue
            ef = x['valor_c'] - x['correto_c']; efeito[t] += ef; qt[t] += 1
            campo, c0, c1, o = {'SUPERAVALIACAO': ('valor_registrado_rs', '', '', ''),
                                'SUBAVALIACAO': ('valor_registrado_rs', '', '', ''),
                                'BAIXADO_MANTIDO': ('status_cadastral/valor', 'excluir da populacao', 'BAIXADO com valor', ''),
                                'CLASSIFICACAO_INCORRETA': ('categoria_cadastrada', x.get('cat_correta', ''), x['cat'], ''),
                                'DUPLICIDADE_CADASTRAL': ('registro inteiro', 'inexistente', 'copia de bem existente',
                                                          orig_id.get(x['bem'], ''))}[t]
            w.writerow([x['id'], t, campo, c0, c1, f"{x['correto_c'] / 100:.2f}", f"{x['valor_c'] / 100:.2f}",
                        f"{ef / 100:.2f}", o])
    total_reg = sum(x['valor_c'] for x in reg); total_ref = sum(x['correto_c'] for x in reg)
    ponte = {'saldo_publicado_rs': cons / 100, 'total_registrado_base_rs': total_reg / 100,
             'efeito_por_tipo_rs': {t: efeito[t] / 100 for t in tipos}, 'quantidade_por_tipo': qt,
             'efeito_total_rs': (total_reg - total_ref) / 100, 'saldo_referencia_sem_erros_rs': total_ref / 100,
             'confere_ponte': total_reg - sum(efeito.values()) == total_ref}
    pp = os.path.join(resv, S['ponte_erros'])
    json.dump(ponte, open(pp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # resumo NAO revelador (so cenario registrado + integridade)
    por_dist = {e: sum(x['valor_c'] for x in reg if x['dist'] == e) / 100 for e in empresas}
    res = {'versao_gerador': cfg['versao'], 'semente': cfg['semente'],
           'python': platform.python_version(), 'sistema': platform.platform(),
           'executado_em': dt.datetime.now().isoformat(timespec='seconds'), 'duracao_s': round(time.time() - t0, 1),
           'linhas_base_registrada': len(reg), 'linhas_referencia': N,
           'linhas_por_distribuidora_referencia': dict(zip(empresas, cotas)),
           'fator_escala_por_distribuidora': {e: round(v, 8) for e, v in fatores.items()},
           'total_registrado_rs': total_reg / 100, 'saldo_publicado_rs': cons / 100,
           'diferenca_rs': (total_reg - cons) / 100, 'total_registrado_por_distribuidora_rs': por_dist,
           'sha256': {os.path.relpath(p, AQUI): sha256(p) for p in (pb, pr, pe, pp)},
           'bytes': {os.path.relpath(p, AQUI): os.path.getsize(p) for p in (pb, pr, pe, pp)},
           'aviso': 'Arquivos em ' + S['reservado_dir'] + ' contem a verdade dos erros: nao usar nos testes de deteccao.'}
    json.dump(res, open(caminho(S['resumo_execucao']), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in res.items() if k not in ('sistema',)}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()

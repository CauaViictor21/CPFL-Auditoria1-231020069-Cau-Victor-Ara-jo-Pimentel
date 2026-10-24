# -*- coding: utf-8 -*-
"""B12 — números citados com 'DF25 ... p. N' conferidos no texto da página física N (±1) da DF25.
Páginas-imagem (34–40) foram transcritas visualmente: não verificáveis por texto (marcadas)."""
import re, sys, json
pg = open('/tmp/claude-0/df25.txt', encoding='utf-8').read().split('\f')
md = open(sys.argv[1], encoding='utf-8').read()
IMG = set(range(33, 41))
def norm(s): return s.replace('.', '')
res = []
for unit in re.split(r'\n(?=\|)|(?<=[.;])\s+(?=[A-ZÁÉÓ])|\n\n', md):
    if 'DF25' not in unit and 'nota' not in unit.lower(): continue
    pages = [int(a) for a in re.findall(r'\bp\.\s*(\d{2,3})(?:/\d+)?', unit) if 20 <= int(a) <= 115]
    if not pages: continue
    nums = [x for x in re.findall(r'(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d])', unit)]
    for x in set(nums):
        rng = set(p for q in pages for p in (q-1, q, q+1))
        if rng & IMG and not any(norm(x) in norm(pg[p-1]) for p in rng if p <= len(pg)):
            st = 'imagem (transcrição visual)'
        else:
            st = 'ok' if any(x in pg[p-1] or norm(x) in norm(pg[p-1]) for p in rng if 1 <= p <= len(pg)) else 'não localizado'
        res.append(dict(numero=x, paginas=sorted(set(pages)), estado=st, ctx=unit[:200].replace('\n', ' ')))
seen = {}; 
for r in res: seen[(r['numero'], tuple(r['paginas']))] = r
res = list(seen.values())
c = {}
for r in res: c[r['estado']] = c.get(r['estado'], 0) + 1
print(c)
json.dump(res, open('/root/cpfl/revisao_b12/check_fontes_df25.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for r in res:
    if r['estado'] == 'não localizado': print(r['numero'], r['paginas'], '::', r['ctx'][:150])

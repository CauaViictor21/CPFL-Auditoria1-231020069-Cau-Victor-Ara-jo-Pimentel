# -*- coding: utf-8 -*-
"""B12 — conferência automatizada de itens normativos citados × página do consolidado (NORMAS)."""
import re, json, sys
t = open('/root/cpfl/fontes/normas.txt', encoding='utf-8').read().split('\f')
md = open(sys.argv[1], encoding='utf-8').read()
def has_item(n, pages):
    pat = re.compile(r'(?m)^\s{0,8}%s\.\s' % n)
    return any(pat.search(t[p-1]) for p in pages if 1 <= p <= len(t))
res = []
# padrão 1: "N (texto; p. P)" ou "N–M (texto; p. P–Q)" dentro de campos de norma
for m in re.finditer(r'(?<![\d.])(\d{1,2})(?:[–-](\d{1,2}))?\s*\(([^()]{0,160}?)\bp\.\s*(\d{3})(?:[–-](\d{3}))?\)', md):
    a, b, txt, p1, p2 = m.group(1), m.group(2), m.group(3), int(m.group(4)), int(m.group(5) or m.group(4))
    pages = list(range(p1, p2+1))
    ok = has_item(a, pages) or has_item(a, [p1-1])  # item pode começar na página anterior
    res.append(dict(tipo='faixa', item=a + (('–'+b) if b else ''), paginas=f'{p1}-{p2}', ok=ok, exato=has_item(a,pages), ctx=md[max(0,m.start()-60):m.end()].replace('\n',' ')))
# padrão 2: "item(ns) N ... NORMAS p. P"
for m in re.finditer(r'itens? (\d{1,2})(?:[–-]\d{1,2})?[^()\n]{0,50}?NORMAS p\.\s*(\d{3})(?:[–-](\d{3}))?', md):
    a, p1, p2 = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
    pages = list(range(p1, p2+1))
    res.append(dict(tipo='item-NORMAS', item=a, paginas=f'{p1}-{p2}', ok=has_item(a, pages) or has_item(a,[p1-1]), exato=has_item(a,pages), ctx=md[max(0,m.start()-60):m.end()].replace('\n',' ')))
# dedup
seen=set(); out=[]
for r in res:
    k=(r['item'],r['paginas'],r['ctx'][-80:])
    if k in seen: continue
    seen.add(k); out.append(r)
json.dump(out, open('/root/cpfl/revisao_b12/check_normas.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
bad=[r for r in out if not r['ok']]; near=[r for r in out if r['ok'] and not r['exato']]
print('citações verificadas', len(out), '| não localizadas', len(bad), '| item começa na página anterior', len(near))
for r in bad: print('X', r['item'], r['paginas'], '::', r['ctx'][-170:])

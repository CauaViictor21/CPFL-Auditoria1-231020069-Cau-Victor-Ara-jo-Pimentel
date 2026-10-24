# -*- coding: utf-8 -*-
"""PTs do Bloco 04: 240, 250, 300, 315, 320, 330 (+ seção de programas por ciclo)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b04_dados import RISCOS, RESPOSTAS, PROGRAMAS, FRAUDE, LEIS, CRONOGRAMA

PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "22/10/2026"
PLAN = "CPFL_B04_Planejamento_Riscos_Materialidade.xlsx"

def fmt(v):
    return f"{v:,.0f}".replace(",", ".") if isinstance(v, (int, float)) else "—"

def tab(header, rows):
    L = [max(8, len(str(h)) + 2, *[min(len(str(r[j])), 60) for r in rows]) for j, h in enumerate(header)]
    tot = sum(min(l, 60) for l in L) or 1
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["-" * max(7, round(100 * min(l, 60) / tot)) for l in L]) + "|"]
    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return "\n".join(out)

PTS = []

# --------------------------------------------------------------------------- 240
PTS.append(dict(
codigo="PT 240", titulo="Responsabilidade do auditor em relação a fraude",
norma="NBC TA 240 (R1) (DOU 05/09/2016), na numeração vigente após a 'Revisão NBC 3' (NORMAS p. 146–188). A NBC TA 315 (R2) item 12(l) remete ao item 28. Itens: 27 (presunção de fraude na receita), 28 (fraude = risco significativo), 32–33 (burla de controles; lançamentos, estimativas e transações incomuns), 48 (documentar refutação). A NBC TA 240 (R2), de 2026, não se aplica a 2025 (D-B01-02).",
objetivo="Identificar fatores de risco de fraude na CPFL, avaliar a presunção de fraude no reconhecimento de receita, tratar o risco de burla de controles pela administração e planejar os testes de lançamentos contábeis e as demais respostas.",
conta="Receita operacional (44.367.780; DRE p. 36/4), receita não faturada (1.763.858; p. 28), estimativas (notas 11, 15, 7, 22) e lançamentos de fechamento.",
afirmacoes="Ocorrência, corte e exatidão da receita (R03 e R04); avaliação das estimativas (R01, R02, R07); todas as afirmações quanto à burla (R16). Riscos significativos por fraude: R03 e R16.",
populacao=f"DF25 p. 27–29 (PAA), 39 (DFC), 54 (nota 3.11), 82–85 (covenants), 100–101 (nota 26), 103 (nota 31), 113 (nota 37); regimentos de governança (Drive pasta 03); planilha {PLAN}, aba Fraude_240.",
procedimentos=[
 ("240-01","Identificar fatores de risco de fraude (incentivos/pressões, oportunidades, atitudes) com fontes públicas","Realizado com evidência pública"),
 ("240-02","Avaliar a presunção de fraude na receita, por tipo de receita (item 27)","Realizado com evidência pública"),
 ("240-03","Discussão da equipe e indagações à administração, à auditoria interna e ao Comitê de Auditoria","Planejado por falta de acesso"),
 ("240-04","Testar lançamentos contábeis e ajustes de fim de período (item 33(a))","Planejado por falta de acesso; critérios aplicados à base sintética no PT 530"),
 ("240-05","Revisão retrospectiva de estimativas 2024 → 2025 (item 33(b))","Realizado com evidência pública (no PT 540)"),
 ("240-06","Avaliar razão de negócio de transações significativas incomuns (item 33(c))","Realizado com evidência pública (parcial)"),
],
corpo=f"""
**1. Fatores de risco de fraude identificados**

{tab(["Categoria","Fator","Fonte","Natureza"], FRAUDE)}

**2. Presunção de fraude no reconhecimento de receita (item 27)**

| Tipo de receita (nota 26 / 3.11) | Discricionariedade | Avaliação |
|---|---|---|
| Fornecimento faturado (tarifas homologadas pela ANEEL) | Baixa: preço regulado e leitura de medidores | Presunção **refutada** para preço; mantida para volume e corte (ver não faturada) |
| Energia fornecida e **não faturada** (1.763.858) | Alta: estimativa com perdas técnicas e comerciais (DF25 p. 28, 54) | **Risco significativo de fraude** (R03) — ocorrência, corte e exatidão |
| Ajuste a valor justo do ativo financeiro (VNR, 1.285.173 na receita) | Alta: estimativa | Tratado como risco significativo de estimativa (R01) e de viés |
| Comercialização (contratos bilaterais na CCEE) | Média: preço de mercado e registro de contratos | Risco mantido; testes de corte (planejado) |
| Receita de construção (5.879.424) | Média: margem e estágio de obra | Conciliar com adições do ativo contratual (R04) |
| Subsídios da CDE (3.103.700) | Baixa: valores definidos pela ANEEL | Presunção refutada; analítico |

A refutação parcial é documentada conforme o item 48: as tarifas e os subsídios são fixados por ato regulatório, o que reduz a oportunidade de manipular o preço. A presunção continua para volume, corte e estimativas.

**3. Burla de controles pela administração (itens 32–33)**

O risco existe em todas as entidades e é tratado como significativo (R16). Respostas obrigatórias planejadas:

- **(a) Lançamentos contábeis.** Critérios de seleção: lançamentos manuais; lançamentos de fim de período e pós-fechamento; contas pouco usadas; valores redondos; lançamentos feitos por usuários não habituais; contrapartidas incomuns, como receita contra conta de ativo regulatório. Sem acesso ao razão, o teste fica *planejado*. Os critérios de seleção serão demonstrados na base sintética (PT 530), com rótulo [S].
- **(b) Revisão retrospectiva de estimativas.** Comparar 2024 com o realizado em 2025: VNR (ajuste de 1.104.267 em 2024 e 1.285.173 em 2025; nota 11), PDD (416.808 → 361.253) e provisões (nota 22). Execução no PT 540.
- **(c) Transações significativas incomuns.** Mútuos com partes relacionadas, que subiram de 2.485.694 para 4.412.650 (BP p. 35/3), e a liquidação antecipada de 5.616.000 em debêntures (nota 19, p. 85). Razão de negócio avaliada nos PT 550 e 570.

**4. Comunicações planejadas.** Indícios de fraude seriam comunicados à governança (PT 260). Não foi identificado indício de fraude em fontes públicas. Fator de risco não é alegação.
""",
evidencias=f"DF25 p. 27–29, 39, 54, 82–85, 100–101, 103, 113; {PLAN} (abas Fraude_240 e Respostas_330). Referências cruzadas: PT 315 (R03, R16), PT 330, PT 540 (revisão retrospectiva), PT 550, PT 530 (critérios de lançamentos na base sintética), PT 260.",
resultados="Dois riscos significativos de fraude: R03 (receita não faturada) e R16 (burla). Presunção de receita refutada só para preço tarifário e CDE, com fundamento documentado. Nenhum indício de fraude identificado nas fontes públicas.",
conclusao="Os riscos de fraude foram identificados e ligados a respostas específicas. Os testes de lançamentos dependem de acesso ao razão e permanecem planejados.",
limitacoes="Sem entrevistas, sem razão contábil e sem acesso a canais de denúncia. O FR 2025 do Drive está truncado; os itens de remuneração e controles não foram lidos (DV15). A avaliação de 'atitudes' não é possível com fontes públicas.",
))

# --------------------------------------------------------------------------- 250
PTS.append(dict(
codigo="PT 250", titulo="Consideração de leis e regulamentos",
norma="NBC TA 250 (DOU 14/02/2019; NORMAS p. 189–202). Itens: 13 (entendimento da estrutura legal), 14 (efeito direto: evidência apropriada), 15 (outras leis: indagação e inspeção de correspondência com reguladores), 19–22 (indícios: entendimento, discussão, avaliação de implicações), 23–29 (comunicação).",
objetivo="Mapear as obrigações legais e regulatórias relevantes da CPFL, distinguir as de efeito direto nas DF das demais, e definir procedimentos e comunicações diante de indícios de descumprimento.",
conta="Receita regulada, ativos e passivos setoriais, ativo financeiro da concessão, tributos e contingências.",
afirmacoes="Divulgação e avaliação de contingências (R07); avaliação e classificação de itens regulatórios (R09, R18, R19).",
populacao=f"DF25 notas 2.1, 8, 22, 26 e 37 (p. 45, 62–63, 94–96, 100–101, 113); Fato Relevante de 08/05/2026; políticas no Drive (pasta 03); {PLAN}, aba Leis_250.",
procedimentos=[
 ("250-01","Mapear leis de efeito direto e outras leis relevantes, com a fonte de cada uma","Realizado com evidência pública"),
 ("250-02","Ler as divulgações de contingências e regulação (notas 22, 26, 37)","Realizado com evidência pública"),
 ("250-03","Indagar a administração e inspecionar correspondência com ANEEL, CVM e Receita Federal (item 15)","Planejado por falta de acesso"),
 ("250-04","Validar bases CCEE/ONS antes de qualquer uso (indicador não prova infração)","Planejado por falta de acesso — pendência P07 da etapa 5"),
],
corpo=f"""
**1. Mapa de leis e regulamentos**

{tab(["Categoria","Lei / regulamento","Fonte","Efeito nas DF","Procedimento"], LEIS)}

**2. Situações já divulgadas que exigem atenção**

- **Ação da ABRADEE** sobre a REN ANEEL 463/2011 (ultrapassagem de demanda e excedente de reativos). Ainda aguarda laudo pericial e julgamento. Os valores estão provisionados como obrigações especiais e passivos setoriais (nota 26.1, p. 100–101).
- **Curtailment** (Lei 15.269/2025). Nenhum valor foi reconhecido, porque as condições do termo de compromisso ainda são incertas (nota 37.2, p. 113). É um potencial ativo contingente, que exige avaliação da divulgação.
- **Processos possíveis.** Entre eles, uma ação ambiental com perda possível de R$ 51.712 mil na CPFL Paulista e execuções fiscais (nota 22, p. 95).

**3. Procedimentos e comunicação diante de indícios (itens 19–29)**

Diante de um indício, os passos planejados são:

1. entender a natureza e as circunstâncias do ato (item 19);
2. discutir com a administração e, se necessário, com a governança (item 20);
3. avaliar o efeito nas DF e na avaliação de riscos, inclusive na confiabilidade das representações (item 22);
4. comunicar ao Comitê de Auditoria (PT 260) e avaliar a necessidade de reportar a autoridades, conforme a lei.

**Neste trabalho não haverá comunicação real a ninguém.**
""",
evidencias=f"DF25 p. 45, 62–63, 94–96, 100–101, 113; Fato Relevante 08/05/2026; {PLAN} aba Leis_250. Referências cruzadas: PT 315 (R07, R09, R18, R19), PT 501 (litígios), PT 260, PT 580.",
resultados="Nove grupos de normas mapeados (5 de efeito direto e 4 outras). Não foi identificado, em fonte pública, indício de descumprimento não divulgado.",
conclusao="O ambiente é altamente regulado; as normas de efeito direto (ANEEL, tributárias, CVM e contratos de concessão) concentram os riscos. Procedimentos de indagação e inspeção de correspondência permanecem planejados.",
limitacoes="Não é parecer jurídico. Sem acesso a correspondência com reguladores. As bases ONS/CCEE do Drive não foram validadas e não foram usadas.",
))

# --------------------------------------------------------------------------- 300
PTS.append(dict(
codigo="PT 300", titulo="Planejamento — estratégia global, plano, cronograma e programas por ciclo",
norma="NBC TA 300 (R1) (DOU 05/09/2016; NORMAS p. 237–251). Itens: 7–8 (estratégia global: alcance, época, direção), 9 (plano de auditoria), 10 (atualização), 12 (documentação), 13 (auditoria inicial). Comentários didáticos com exemplos de outra companhia no consolidado foram ignorados.",
objetivo="Definir a estratégia global e o plano de auditoria das DF consolidadas de 2025 da CPFL, com cronograma e programas por ciclo, justificando prioridades e alterações.",
conta="DF consolidadas 2025 (todas as classes significativas).",
afirmacoes="Ver matriz do PT 315 (19 riscos; 4 significativos).",
populacao=f"Resultados dos PT EC–230, PT 315 e PT 320; {PLAN}, abas Programas_Ciclos e Cronograma_300.",
procedimentos=[
 ("300-01","Definir características do trabalho, objetivos de relatório, fatores significativos e recursos (item 8)","Realizado com evidência pública"),
 ("300-02","Elaborar o plano: avaliação de riscos, procedimentos adicionais e outros (item 9)","Realizado com evidência pública"),
 ("300-03","Elaborar os 6 programas por ciclo com a aplicabilidade fundamentada","Realizado com evidência pública — programas elaborados; execução registrada nos PTs seguintes"),
 ("300-04","Registrar alterações de planejamento (item 10)","Realizado com evidência pública — controle de versões (PT 230)"),
],
corpo=f"""
**1. Estratégia global (itens 7–8)**

| Elemento | Definição |
|---|---|
| Alcance | DF individuais e consolidadas de 2025 (perímetro principal: consolidado), com práticas contábeis adotadas no Brasil e IFRS. Companhia listada (Novo Mercado): relatório com PAA (NBC TA 701, fora do escopo deste dossiê) |
| Época | Planejamento em 22/10/2026; execução até 25/10/2026. Em uma auditoria real: interina no 4º trimestre e final em jan–fev, com relatório em 04/03/2026 |
| Direção e prioridades | (1) ativo financeiro da concessão (36,5% do ativo; PAA 3); (2) ativo contratual (PAA 1); (3) receita não faturada (PAA 2) e fraude; (4) dívida e covenants; (5) grupo (PT 600) |
| Materialidade | Global 404.562,30; execução 303.421,73; trivial 20.228,12 (PT 320) |
| Abordagem | **Substantiva**: não há testes de controles possíveis. RDR = risco inerente (315 item 34) |
| Recursos | Aluno + IA. Em auditoria real seriam necessários especialistas em avaliação (VNR), TI (faturamento) e tributos (PT 220) |
| Auditoria inicial (item 13) | Tratada como didática: saldos de abertura no PT 510 |

**2. Programas por ciclo (resumo; detalhes na planilha)**

{tab(["Código","Ciclo","Riscos","Saldo-base","Aplicabilidade e extensão"], [(c, ci, rs, sb, ap) for c, ci, rs, sb, ap, _ in PROGRAMAS])}

Os procedimentos de cada programa estão na seção 6 do dossiê e na aba Programas_Ciclos.

**3. Cronograma**

{tab(["Fase","Data","Bloco","PTs"], CRONOGRAMA)}

**4. Justificativa de prioridades e alterações**

As prioridades seguem o peso no ativo e os PAA do auditor real. O estoque recebe extensão reduzida, porque está abaixo da materialidade global e não tem risco qualitativo identificado, mas é mantido com análise fundamentada (enunciado). Alteração registrada: inclusão de R18 (renovação das concessões) e R19 (PIS/COFINS sobre ICMS) na matriz preliminar. Correção do saldo de R08 (DV17).
""",
evidencias=f"{PLAN}; PT 315; PT 320; PT 330; DF25 p. 26–36. Referências cruzadas: todos os PTs dos blocos 05–11.",
resultados="Estratégia e plano documentados; 6 programas com aplicabilidade fundamentada (estoques com extensão reduzida e justificativa).",
conclusao="O plano direciona o esforço para as estimativas da concessão e para a receita, com abordagem substantiva compatível com a ausência de acesso a controles.",
limitacoes="O plano real de uma firma incluiria horas, equipe e datas de campo, que não se aplicam aqui. A abordagem substantiva pura é uma limitação: em uma companhia desse porte, controles seriam testados.",
))

# --------------------------------------------------------------------------- 315
rows315 = [(i, c, fmt(s), af, fa, f"{p}×{m}", nv, sig) for (i, c, s, fo, af, ri, fa, p, m, nv, sig, fu) in RISCOS]
PTS.append(dict(
codigo="PT 315", titulo="Identificação e avaliação dos riscos de distorção relevante",
norma="NBC TA 315 (R2) (DOU 02/09/2021; aplicável a períodos iniciados a partir de 01/01/2022 — item 10, NORMAS p. 256). Itens: 12(f) fatores de risco inerente, 12(l) risco significativo, 19 (entidade, ambiente e estrutura contábil), 21–27 (componentes do controle interno, inclusive TI — 25–26), 28–29 (riscos e afirmações relevantes), 31 (risco inerente: probabilidade e magnitude), 32 (riscos significativos), 33 (riscos em que só substantivos não bastam), 34 (risco de controle).",
objetivo="Compreender a entidade, o ambiente, a estrutura contábil, a TI e os controles. Elaborar a matriz de riscos por conta e afirmação e identificar riscos significativos.",
conta="Todas as classes de transações, saldos e divulgações significativas do consolidado 2025.",
afirmacoes="Ver matriz: 19 riscos; 4 significativos (R01, R02, R03, R16).",
populacao=f"Memorando da entidade (seção 3 do dossiê); DF25 notas e PAA; matriz preliminar da etapa 3 (17 riscos, revista); {PLAN}, aba Matriz_Riscos_315.",
procedimentos=[
 ("315-01","Entendimento da entidade, do ambiente e da estrutura contábil (item 19)","Realizado com evidência pública (memorando, B02)"),
 ("315-02","Entendimento dos componentes do controle interno e da TI (itens 21–27)","Realizado com evidência pública (entendimento) / Planejado por falta de acesso (walkthroughs)"),
 ("315-03","Identificar riscos e afirmações relevantes; avaliar o risco inerente por fatores (itens 28–31)","Realizado com evidência pública"),
 ("315-04","Determinar riscos significativos (item 32) e riscos em que só substantivos não bastam (item 33)","Realizado com evidência pública"),
 ("315-05","Revisar a matriz preliminar da etapa 3 com fontes primárias","Realizado com evidência pública — saldos reconferidos; R08 corrigido (DV17); R18 e R19 incluídos"),
],
corpo=f"""
**1. Entendimento do controle interno (itens 21–27): o que se sabe publicamente**

| Componente | Evidência pública | Lacuna |
|---|---|---|
| Ambiente de controle | Novo Mercado; Conselho de Administração, Comitê de Auditoria (regimentos de 11/11/2025 e 08/09/2026) e Conselho Fiscal (regimento de 10/05/2024) — Drive pasta 03 | Cultura e tom da administração não observáveis |
| Avaliação de riscos da entidade | Política de Gerenciamento de Riscos publicada (Drive pasta 03); nota 33 (gestão de riscos, p. 105–107) | FR item 4 indisponível (truncado) |
| Sistema de informação (TI) | Faturamento por leitura e rota; estimativa por carga e perdas (nota 3.11, p. 54); a PwC usou especialistas de TI (p. 28) | Sistemas, interfaces e ITGC desconhecidos |
| Atividades de controle | A PwC avaliou desenho e implementação de controles da receita não faturada e da bifurcação de ativos (p. 28–29) | Nenhum controle identificado diretamente |
| Monitoramento | Regulamento de Auditoria Interna (24/01/2024, Drive pasta 03) | Relatórios internos indisponíveis |

**2. Matriz de riscos (resumo; detalhes, fontes e fundamentos na planilha)**

{tab(["ID","Conta / processo","Saldo (R$ mil)","Afirmações","Fatores*","Prob.×Magn.","Nível","Significativo?"], rows315)}

*C = complexidade; S = subjetividade; M = mudança; I = incerteza; V = viés/fraude (item 12(f)).

**3. Riscos significativos (item 32)**

- **R01** ativo financeiro da concessão;
- **R02** ativo contratual;
- **R03** receita não faturada, que também é risco de fraude (240 item 28);
- **R16** burla de controles.

**4. Riscos em que só procedimentos substantivos não bastam (item 33).** R03 e R15: a receita não faturada depende de grandes volumes de dados processados por sistemas. Numa auditoria real, isso exigiria testar ITGC e controles de interface. Neste trabalho é uma **limitação** relevante, registrada no PT 330.

**5. Riscos no nível das demonstrações.** Burla de controles (R16); complexidade do grupo (R14); dependência de regulação (renovação das concessões, R18).
""",
evidencias=f"{PLAN} (Matriz_Riscos_315); DF25 p. 27–29, 34–36, 54, 61–68, 75–85, 94–113; regimentos e políticas (Drive pasta 03). Referências cruzadas: PT 240, PT 250, PT 320, PT 330, PT 540, PT 600.",
resultados="19 riscos avaliados (4 altos/significativos, 12 moderados, 3 baixos). Matriz preliminar revista: saldos conferidos com a DF25, R08 corrigido (DV17) e dois riscos novos.",
conclusao="Os riscos se concentram nas estimativas da concessão e na receita estimada, coerentes com os três PAA do auditor real. Sem teste de controles, o risco de distorção relevante equivale ao risco inerente (item 34).",
limitacoes="Avaliação baseada em documentos públicos; sem walkthroughs. Pontuação por probabilidade×magnitude é uma aproximação didática do espectro. O FR truncado impediu a leitura dos fatores de risco declarados pela companhia (item 4 do FR).",
))

# --------------------------------------------------------------------------- 320
PTS.append(dict(
codigo="PT 320", titulo="Materialidade no planejamento e na execução",
norma="NBC TA 320 (R1) (DOU 05/09/2016; NORMAS p. 367–378). Itens: 10 (global e específicas), 11 (execução), 12–13 (revisão), 14 (documentação), A3–A13 (referenciais; A8 cita 5% do lucro antes do imposto como exemplo).",
objetivo="Calcular e justificar a materialidade global, a materialidade para execução e o limite de distorções claramente triviais, e avaliar a necessidade de materialidades específicas.",
conta="DF consolidadas 2025 como um todo.",
afirmacoes="Não se aplica por afirmação; a materialidade orienta o PT 315 (saldo/MG) e o PT 330 (extensão).",
populacao=f"Planilha e relatório metodológico da etapa 2 (reaproveitados); bases reconferidas na DF25 (B02); {PLAN}, aba Materialidade.",
procedimentos=[
 ("320-01","Reconferir as bases (LAIR, receita, ativo, PL, VNR) na DF25","Realizado com evidência pública — sem divergência"),
 ("320-02","Comparar referenciais e escolher a base","Realizado com evidência pública"),
 ("320-03","Calcular global, execução e trivial com fórmulas","Realizado com evidência pública"),
 ("320-04","Analisar sensibilidade (VNR; execução 60% e 50%)","Realizado com evidência pública"),
 ("320-05","Avaliar materialidades específicas (item 10)","Realizado com evidência pública — nenhuma quantitativa (fundamento abaixo)"),
],
corpo="""
**1. Referenciais comparados (R$ mil)**

| Referencial | Base | % | Resultado | Fonte |
|---|---|---|---|---|
| Lucro antes dos tributos | 8.091.246 | 5% | **404.562,30** | DF25 p. 36/4 |
| Receita líquida | 44.367.780 | 0,5% | 221.838,90 | DF25 p. 36/4 |
| Ativo total | 81.099.930 | 0,5% | 405.499,65 | DF25 p. 34/2 |
| Patrimônio líquido | 23.504.510 | 1% | 235.045,10 | DF25 p. 35/3 |

**Escolha:** LAIR. A companhia é lucrativa e o lucro é estável (8.088.893 em 2024), e o lucro é a medida de foco dos acionistas de uma companhia listada. O percentual de 5% é julgamento: a NBC TA 320 item A8 o cita **como exemplo** para entidades com fins lucrativos, não como regra.

**2. Valores adotados**

| Medida | Valor (R$ mil) | Critério |
|---|---|---|
| Materialidade global | 404.562,30 | 5% do LAIR |
| Materialidade para execução | 303.421,73 | 75% da global — julgamento aprovado na etapa 2 e validado pelo aluno em 22/10/2026 (D-B04-01) |
| Claramente trivial | 20.228,12 | 5% da global (limite operacional para a NBC TA 450) |

**3. Sensibilidade**

- Excluindo mecanicamente o ajuste VNR (1.285.173, que é não caixa e decorre de estimativa), a global cairia para 340.303,65, uma redução de 64.258,65.
- A execução a 60% daria 242.737,38; a 50%, 202.281,15.

**Julgamento:** manter 75%. Não há histórico conhecido de distorções, o relatório de 2025 não tem modificação e não há reapresentação identificada. O caráter de auditoria inicial (PT 510) é o principal argumento para reduzir. Se o PT 510 revelar ajustes de abertura, a execução será revista para 60%.

**4. Materialidades específicas (item 10)**

Nenhuma é fixada quantitativamente. As divulgações sensíveis aos usuários, como remuneração da administração e transações com o controlador, são avaliadas qualitativamente (PT 450 e PT 550). As estimativas de maior risco recebem resposta extensiva, não materialidade menor.

**5. Revisão (itens 12–13)**

Gatilhos documentados na planilha: distorções acumuladas acima de 50% da execução; eventos que alterem o LAIR; ajustes de abertura.
""",
evidencias=f"{PLAN} (aba Materialidade, 21 fórmulas); planilha e PDF da etapa 2 (Drive, MANDAR PARA O CLAUDE PRO); DF25 p. 34–36, 68. Referências cruzadas: PT 315 (coluna Saldo/MG), PT 330, PT 450, PT 510, PT 530 (erro tolerável).",
resultados="Bases da etapa 2 conferidas com a DF25 sem divergência. Valores mantidos: 404.562,30 / 303.421,73 / 20.228,12.",
conclusao="Materialidade definida e fundamentada como julgamento, com sensibilidade e gatilhos de revisão.",
limitacoes="Percentuais são julgamentos didáticos. A materialidade efetivamente usada pela PwC não é pública, então não houve comparação.",
))

# --------------------------------------------------------------------------- 330
resp_rows = []
for rid, lst in RESPOSTAS.items():
    for pr, nat, ep, ext, mod, pt in lst:
        resp_rows.append((rid, pr, nat, ext, mod, pt))
PTS.append(dict(
codigo="PT 330", titulo="Respostas do auditor aos riscos avaliados",
norma="NBC TA 330 (R1) (DOU 05/09/2016; NORMAS p. 379–403). Itens: 5 (respostas gerais), 6–7 (procedimentos adicionais por afirmação), 15 (controles sobre riscos significativos), 18 (substantivos para cada classe significativa), 19 (confirmação externa), 21 (riscos significativos: substantivos específicos), 25–27 (suficiência), 28–30 (documentação).",
objetivo="Relacionar cada risco avaliado a testes de controles e procedimentos substantivos, definindo natureza, época e extensão e distinguindo testes executados de planejados.",
conta="Todas as classes significativas (PT 315).",
afirmacoes="Conforme a matriz do PT 315.",
populacao=f"{PLAN}, aba Respostas_330 (33 respostas para 19 riscos).",
procedimentos=[
 ("330-01","Definir respostas gerais no nível das demonstrações (item 5)","Realizado com evidência pública"),
 ("330-02","Definir respostas por risco e afirmação, com natureza, época, extensão e modalidade (itens 6–7)","Realizado com evidência pública"),
 ("330-03","Garantir substantivos para cada classe significativa (item 18) e específicos para riscos significativos (item 21)","Realizado com evidência pública — verificado na matriz"),
 ("330-04","Avaliar a suficiência da evidência ao final (itens 25–27)","Realizado com evidência pública — matriz de suficiência do PT 500 (Bloco 11); insuficiente em R02, R03 e R16"),
],
corpo=f"""
**1. Respostas gerais (item 5)**

- Ceticismo reforçado nas estimativas.
- Reconferência de toda fonte secundária, que já identificou DV01 e DV11–DV13.
- Imprevisibilidade: seleção amostral aleatória com semente registrada.
- Abordagem **substantiva**, porque não há acesso a controles.

**2. Respostas por risco**

{tab(["Risco","Procedimento","Natureza","Extensão","Modalidade","PT"], resp_rows)}

**3. Verificação de cobertura**

- Todos os 19 riscos têm pelo menos uma resposta.
- Os 4 riscos significativos têm procedimentos substantivos específicos (item 21).
- Toda classe significativa tem procedimento substantivo (item 18).
- Os testes de controles foram **planejados** para R03 e R15, onde só substantivos não bastam (315 item 33). Sem acesso, **essa insuficiência é uma limitação do trabalho**, não uma conclusão sobre os controles da CPFL.

**4. Situação de execução em 22/10/2026**

- Executados com evidência pública: conciliações do B02 (CC01–CC07) e a reexecução da nota 11.
- Os demais procedimentos estão planejados ou serão simulados nos blocos 05–10.

**5. Atualização em 23/10/2026 (Bloco 08) — resposta ao risco R01 executada na base sintética**

| Resposta planejada (R01) | Execução | Modalidade |
|---|---|---|
| Testes de detalhes sobre a existência e a avaliação do ativo financeiro da concessão | 4 procedimentos integrais por computador (T1–T4) em 501.000 registros e amostragem MUS de 385 itens, ampliada em 492 itens na população residual (PT 530) | Simulado para fins didáticos |
| Avaliação das distorções identificadas | Distorção conhecida líquida de R$ 117,5 milhões (superavaliação), equivalente a 38,7% da materialidade de execução e 29,0% da global (PT 450) | Simulado para fins didáticos |

- Natureza da resposta: substantiva, sem confiança em controles. Como a abordagem ao risco significativo é só substantiva, ela inclui testes de detalhes (NBC TA 330 item 21, NORMAS p. 384). A extensão segue o risco significativo: 95% de confiança e testes integrais onde o computador permite.
- A amostra inicial **não** bastou (o limite superior de distorção excedeu a distorção tolerável). A extensão foi ampliada antes de qualquer afirmação de suficiência, como pedem a NBC TA 330, item 26 (NORMAS p. 385), e a NBC TA 530, item 15 (p. 536).
- Na CPFL real, a mesma resposta exigiria o cadastro de bens, a base de remuneração homologada e o laudo de VNR. Essa parte continua **Planejado por falta de acesso**.
""",
evidencias=f"{PLAN} (Respostas_330, Programas_Ciclos); CPFL_B02_Dados_Reais_2025.xlsx (Conciliacoes); CPFL_B08_Amostragem_Testes_Distorcoes.xlsx (B08). Referências cruzadas: PT 315, PT 500, PT 505, PT 520, PT 530, PT 540, PT 560, PT 570, PT 600.",
resultados="33 respostas mapeadas: 19 executáveis com evidência pública (várias de forma parcial), 4 simuladas ou com modelos não enviados e 10 planejadas por falta de acesso.",
conclusao="As respostas são proporcionais aos riscos avaliados e ligadas a PTs. A impossibilidade de testar controles sobre a receita não faturada é a principal limitação.",
limitacoes="Época 'interina' e testes de controle são apenas planejados. A suficiência da evidência só será avaliada no B11 (PT 500).",
))

# --------------------------------------------------------------------------- PROGRAMAS (seção própria)
PROG_MD = "\n\n".join(
    f"## {cod} — Programa de auditoria: {ci}\n\n**Riscos:** {rs} · **Saldo-base:** {sb} · **Aplicabilidade:** {ap}\n\n" +
    tab(["Nº","Procedimento e modalidade"], [(k, p) for k, p in enumerate(procs, 1)]) +
    f"\n\nPreparador: {PREP} — {DATA}. Revisão: ____ (em branco)."
    for cod, ci, rs, sb, ap, procs in PROGRAMAS)

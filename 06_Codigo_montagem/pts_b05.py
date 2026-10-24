# -*- coding: utf-8 -*-
"""PTs do Bloco 05: PT 402 e PT 600."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "22/10/2026"
PLAN = "CPFL_B05_Grupo_Prestadores.xlsx"
PTS = []

# --------------------------------------------------------------------------- 402
PTS.append(dict(
codigo="PT 402", titulo="Considerações de auditoria para entidade que utiliza organização prestadora de serviços",
norma="NBC TA 402 (Res. CFC 1.215/2009; NORMAS p. 404–426). Itens: 8 (definições, inclusive controles complementares da entidade usuária), 9–11 (entendimento dos serviços), 12 (procedimentos quando o entendimento é insuficiente: relatório tipo 1 ou tipo 2, contato, visita), 13–14 (suficiência dos relatórios), 15–17 (respostas e efetividade operacional; tipo 2), 18 (organizações subcontratadas).",
objetivo="Identificar serviços terceirizados relevantes para as informações financeiras da CPFL e os controles complementares que a entidade usuária precisa manter. Planejar a análise de relatórios tipo 1 e tipo 2 e os procedimentos alternativos.",
conta="Previdência (obrigação atuarial 606.924; BP p. 35/3), receita e custo de energia liquidados na CCEE, ativo contratual (construção), contas a receber e caixa (arrecadação).",
afirmacoes="Avaliação e existência (previdência); ocorrência e exatidão (CCEE); existência e exatidão (construção); existência e corte (arrecadação). Risco ligado a R03, R06 e R15 do PT 315.",
populacao=f"DF25 notas 3 (p. 47), 3.11 (p. 54), 20 (p. 85–92), 23 (p. 97); nota 13.1 (p. 70) para serviços internos do grupo; {PLAN}, aba Prestadores_402.",
procedimentos=[
 ("402-01","Identificar prestadores e serviços citados nas notas e classificá-los como documentados ou hipóteses","Realizado com evidência pública"),
 ("402-02","Distinguir prestador que integra o sistema de informação (402) de fornecedor operacional (500) e de função interna do grupo (600)","Realizado com evidência pública"),
 ("402-03","Obter e avaliar relatórios tipo 1/tipo 2 (período, exceções, subcontratadas, controles complementares)","Planejado por falta de acesso"),
 ("402-04","Procedimentos alternativos: conciliações, confirmação, relatórios do auditor do plano de previdência, especialista atuário","Planejado por falta de acesso"),
],
corpo="""
**1. Prestadores identificados e tratamento**

| Prestador / serviço | Base documental | Tratamento normativo |
|---|---|---|
| Vivest e Fundação Família Previdência — administração dos planos e dos ativos garantidores | Nota 20 (p. 86 e 92) | **NBC TA 402**: processam informações (ativos do plano e dados de participantes) que entram nas DF |
| CCEE — contabilização e liquidação do mercado de curto prazo | Nota 3.11 (p. 54) | **NBC TA 402 por analogia**: os relatórios de liquidação alimentam receita e custo de energia. A existência de relatório de asseguração da CCEE não foi verificada |
| Agentes arrecadadores (bancos) e convênios de arrecadação | Nota 23 (p. 97); bancos são hipótese | **NBC TA 402** se os arquivos de retorno bancário forem a base da baixa de recebíveis |
| Empreiteiras de construção ("alto grau de terceirização") | Nota 3 (p. 47) | **Não é NBC TA 402**: prestador operacional; evidência pela NBC TA 500 (medições e contratos) |
| Provedores de TI/nuvem | Hipótese (não citado na DF25) | NBC TA 402 se houver terceirização de ERP ou faturamento; confirmar por indagação |
| CPFL Serviços, Finanças, Pessoas, Supri, Atende | Entidades do grupo (nota 13.1, p. 70) | **Não é NBC TA 402**: funções compartilhadas tratadas no PT 600 |

**2. Relatórios tipo 1 e tipo 2 (itens 12–17): o que seria exigido**

- **Tipo 1** atesta o desenho e a implementação dos controles do prestador em uma data. Serve ao entendimento (item 14).
- **Tipo 2** atesta também a efetividade operacional ao longo de um período. Só ele serve como evidência para confiar nos controles (itens 16–17).
- Para cada relatório seria preciso verificar:
  - a competência e a independência do auditor do prestador (item 13);
  - a cobertura do período auditado (2025) e as exceções relatadas;
  - os controles complementares que a CPFL deveria manter (item 8), por exemplo a conciliação de contribuições e o envio de cadastro à Vivest;
  - as organizações subcontratadas excluídas do relatório (item 18).

**Nenhum relatório foi obtido. Não se afirma a existência de nenhum deles.**

**3. Procedimentos alternativos planejados**

- **Previdência:** relatório do auditor independente do plano, confirmação dos ativos garantidores e teste dos dados censitários com especialista atuário (NBC TA 620).
- **CCEE:** conciliar relatórios de liquidação com a contabilidade. Os dados abertos da CCEE no Drive só podem ser usados depois de validar a fonte (pendência P07).
- **Arrecadação:** conciliar arquivos de retorno com as baixas de contas a receber e fazer confirmação bancária (PT 505).
""",
evidencias=f"DF25 p. 47, 54, 70, 85–92, 97; {PLAN} (Prestadores_402). Referências cruzadas: PT 315 (R03, R15), PT 330, PT 500, PT 505, PT 540 (premissas atuariais), PT 600 (serviços compartilhados).",
resultados="Seis serviços analisados: três tratados pela NBC TA 402 (previdência, CCEE e arrecadação), um como fornecedor operacional, um como hipótese de TI e um como função interna do grupo. Nenhum relatório tipo 1 ou tipo 2 disponível.",
conclusao="Os serviços terceirizados mais relevantes estão nos planos de previdência e na liquidação de energia. Sem relatórios de asseguração, a evidência sobre esses serviços dependeria de procedimentos alternativos, todos planejados.",
limitacoes="O FR 2025 do Drive está truncado; os itens sobre recursos e terceirização não foram lidos (DV15). A existência de terceirização de TI não foi verificada.",
))

# --------------------------------------------------------------------------- 600
PTS.append(dict(
codigo="PT 600", titulo="Auditoria de demonstrações contábeis de grupo",
norma="NBC TA 600 (R2) (DOU 06/12/2023; aplicável a períodos iniciados a partir de 01/01/2024 — item 12, NORMAS p. 688). Itens: 13 (objetivos), 14 (definições: componente, auditor do componente, risco de agregação), 17 (aceitação), 22 (estratégia: onde executar trabalho e envolvimento de auditores de componentes), 24–26 (auditores de componentes: cooperação, ética, competência), 30 (entendimento do grupo e da consolidação), 33 (riscos, inclusive consolidação), 35 (materialidade de execução do componente < execução do grupo; limite de comunicação ≤ trivial do grupo), 37–38 (respostas e consolidação), 45 (comunicações dos auditores de componentes), 49 (eventos subsequentes), 57 (comunicação à governança).",
objetivo="Mapear o grupo, seus componentes e a consolidação. Avaliar riscos, definir a materialidade dos componentes, planejar o envolvimento de auditores de componentes e avaliar a suficiência da evidência.",
conta="DF consolidadas 2025 (ativo 81.099.930; LAIR 8.091.246) e investimentos da controladora (22.675.914; BP p. 34/2).",
afirmacoes="Integridade e apresentação da consolidação (R14); eliminações intragrupo; equivalência patrimonial de controladas em conjunto (380.803; BAESA e Chapecoense) e o julgamento de controle conjunto da Chapecoense; reorganizações societárias.",
populacao=f"DF25 nota 1 (p. 41–42), nota 13 (p. 69–74, inclusive 13.9.3 na p. 74), nota 30 (p. 103), nota 37.1 (p. 113); DF 2025 das controladas Paulista, RGE, Piratininga, Transmissão e Renováveis (Drive pasta 06); {PLAN}.",
procedimentos=[
 ("600-01","Mapear estrutura do grupo, natureza de cada participação e método contábil","Realizado com evidência pública"),
 ("600-02","Dimensionar componentes por ativo e resultado (nota 13.1) e por segmento (nota 30), com conciliação","Realizado com evidência pública — nota 30 concilia com o total"),
 ("600-03","Identificar riscos da consolidação e das reorganizações de 2025–2026","Realizado com evidência pública"),
 ("600-04","Definir materialidade de execução dos componentes e limite de comunicação (item 35)","Realizado com evidência pública (julgamento documentado)"),
 ("600-05","Identificar auditores dos componentes e opiniões emitidas","Realizado com evidência pública (5 controladas)"),
 ("600-06","Enviar instruções aos auditores de componentes e obter comunicações (itens 24–26, 45)","Planejado por falta de acesso — modelo de instruções não enviado"),
 ("600-07","Testar eliminações e o processo de consolidação (item 38)","Planejado por falta de acesso (sem mapa de consolidação)"),
],
corpo="""
**1. Estrutura do grupo (nota 1, p. 41–42)**

- **Controladas integrais ou majoritárias:**
  - 4 distribuidoras (Paulista, Piratininga, RGE, Santa Cruz);
  - geração (CPFL Renováveis, CPFL Geração, CERAN 65%, ENERCAN 52,12%, Paulista Lajeado 56,93%);
  - transmissão (CPFL Transmissão, TESB 98,01% e as sociedades de transmissão);
  - comercialização (CPFL Brasil e outras) e serviços.
- **Controladas em conjunto (equivalência patrimonial; nota 13.9.3, p. 74):** BAESA (25,01%) e Chapecoense (51%, controladora da Foz do Chapecó). O investimento total no consolidado é de 380.803 (BP p. 34/2).
  - **Julgamento relevante:** mesmo com mais de 50% das ações da Chapecoense, a CPFL Geração a trata como controle conjunto com base no acordo de acionistas (p. 74).
  - Os empréstimos do BNDES da Chapecoense restringem dividendos acima do mínimo de 25% sem anuência do BNDES (p. 74).
- **Participações minoritárias:** TPAE (9,65%) e ETAU (10%) (nota 1). A classificação contábil não foi verificada; uma possibilidade é a linha "investimentos em instrumentos patrimoniais" (129.659).
- **Controlador:** State Grid Brazil Power Participações S.A. (nota 31, p. 103).

**2. Componentes e porte relativo (nota 13.1, p. 70/38 — dados individuais de cada controlada)**

| Componente | Ativo total | Resultado 2025 | Ativo / consolidado | Resultado / LAIR | Abordagem |
|---|---|---|---|---|---|
| CPFL Paulista | 22.954.592 | 1.864.350 | 28,3% | 23,0% | Informações financeiras completas |
| CPFL RGE | 21.762.223 | 1.327.456 | 26,8% | 16,4% | Informações financeiras completas |
| CPFL Transmissão | 9.425.400 | 268.600 | 11,6% | 3,3% | Ativo contratual (PAA 1) e receita de remuneração |
| CPFL Renováveis | 8.335.380 | 1.062.034 | 10,3% | 13,1% | Imobilizado, intangível e receita de geração |
| CPFL Piratininga | 8.226.299 | 548.281 | 10,1% | 6,8% | Ativo financeiro da concessão, receita e dívida |
| CPFL Brasil | 4.855.998 | 142.279 | 6,0% | 1,8% | Corte da receita de comercialização |
| CPFL Geração | 3.461.790 | 1.129.886 | 4,3% | 14,0% | Analíticos e equivalência patrimonial; incorporada em 02/02/2026 |
| CPFL Santa Cruz | 2.647.005 | 130.563 | 3,3% | 1,6% | Ativo financeiro da concessão + analíticos |

Os valores são individuais e incluem participações em outras controladas, por isso as porcentagens se sobrepõem e não somam 100%. A versão R2 da NBC TA 600 não usa mais a classificação "componente significativo". A escolha dos componentes segue o risco e o risco de agregação (itens 22 e 33).

**3. Segmentos (nota 30, p. 103/71) — conciliação**

A soma de receita, LAIR e aquisições por segmento concilia com o consolidado. A receita difere em R$ 1 mil, por arredondamento.

- A distribuição responde por 65,9% do LAIR e a geração por 31,5%.
- A comercialização teve prejuízo antes dos impostos de 281.094.
- As vendas entre segmentos de 3.330.455 são eliminadas na consolidação.

Um valor da tabela foi lido inicialmente com um dígito errado (aquisições de geração: 269.975, e não 259.975) e foi corrigido pela conciliação.

**4. Riscos da consolidação e de reorganizações (item 33)**

- **Venda da EPASA** (junho/2025): baixa de investimento de 152.888 e despesa líquida de 92.325 (nota 13.4, p. 71).
- **Reestruturações de 2025:**
  - cisão de 1,85% da CPFL Renováveis, que passou a ser controlada direta (nota 13.5);
  - mudança do controle acionário da CPFL Transmissão, com a CPFL Energia passando a deter 51% das ações ordinárias (nota 13.6).
- **Evento posterior:** incorporação da CPFL Geração pela CPFL Brasil em 02/02/2026, sem impacto no consolidado segundo a nota 37.1 (p. 113).
- **Eliminações intragrupo:** vendas entre segmentos de 3.330.455 e resultado financeiro intragrupo de 22.557 (nota 30). Mútuos entre partes relacionadas com o controlador (PT 550).
- **Classificação da Chapecoense como controle conjunto** (51% do capital votante; acordo de acionistas). Se a classificação estivesse errada, mudaria o método de consolidação. Resposta: ler o acordo de acionistas (planejado por falta de acesso).
- **Não controladores:** PL de 1.014.735 e lucro de 258.229 (BP p. 35; DRE p. 36). Exigem divulgação conforme o CPC 45 (nota 13.9).

**5. Materialidade dos componentes (item 35)**

| Medida | Valor (R$ mil) | Critério |
|---|---|---|
| Execução do grupo | 303.421,73 | PT 320 |
| Execução — Paulista e RGE | 212.395,21 | 70% da execução do grupo (inferior a ela, como exige o item 35(a)) |
| Execução — demais componentes | 151.710,86 | 50% da execução do grupo (mais componentes, maior risco de agregação) |
| Limite de comunicação de distorções | 20.228,12 | Igual ao trivial do grupo (item 35(b): não pode excedê-lo) |

Os percentuais de 70% e 50% são julgamento; a norma exige apenas que fiquem abaixo da execução do grupo.

**6. Auditores dos componentes (itens 24–26)**

A PwC emitiu as DF 2025 da CPFL Paulista, Piratininga, Transmissão e Renováveis, com relatórios de 04/03/2026, e da RGE, com opinião sem modificação (data não localizada no texto extraído). É a mesma firma do grupo. Isso facilita a coordenação, mas não dispensa os requisitos de ética, competência e comunicação.

Os auditores da Santa Cruz, CPFL Brasil, CPFL Geração e das controladas em conjunto não foram verificados.

**Modelo didático de instruções ao auditor do componente (NÃO ENVIADO):** escopo e informações financeiras a auditar, materialidade de execução do componente, limite de comunicação de 20.228,12, riscos significativos do grupo que afetam o componente (R01, R03), confirmação de independência e de cooperação (item 24), prazos e comunicações exigidas (item 45), e eventos subsequentes (item 49).

**7. Suficiência da evidência (avaliação preliminar)**

Para os componentes, há apenas evidência pública: as DF auditadas e as opiniões publicadas. Faltam as comunicações dos auditores, a documentação dos trabalhos e o mapa de consolidação. **A evidência é insuficiente para uma conclusão de auditoria de grupo.** A limitação está registrada para o PT 500 e para a conclusão integrada.
""",
evidencias=f"{PLAN} (Componentes_600, Segmentos_nota30); DF25 p. 34–36, 41–42, 69–74, 103, 113; DF das controladas (Drive pasta 06). Referências cruzadas: PT 315 (R14), PT 320, PT 330, PT 402 (serviços compartilhados), PT 550, PT 560 (incorporação 2026), PT 260 (item 57).",
resultados="Grupo mapeado com 8 componentes principais e as controladas em conjunto. A nota 30 concilia com o consolidado (diferença de R$ 1 mil por arredondamento). Materialidades de componente definidas. Cinco relatórios de componentes identificados (PwC, sem modificação).",
conclusao="O risco do grupo se concentra em duas distribuidoras (Paulista e RGE: cerca de 55% do ativo individual somado ao consolidado) e nas reorganizações societárias. A abordagem e a materialidade estão definidas. A evidência sobre componentes é limitada ao que é público.",
limitacoes="Não há mapa de consolidação, comunicação com auditores de componentes nem acesso a eliminações. Os dados de componentes são individuais e se sobrepõem. O FR truncado impediu confirmar a estrutura societária completa e a lista de auditores.",
))

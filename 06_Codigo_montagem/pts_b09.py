# -*- coding: utf-8 -*-
"""PTs do Bloco 09: PT 510, PT 520, PT 540 e PT 550."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "23/10/2026"
PLAN = "CPFL_B09_Abertura_Analiticos_Estimativas_PartesRel.xlsx"
PTS = []

# --------------------------------------------------------------------------- 510
PTS.append(dict(
codigo="PT 510", titulo="Trabalhos iniciais — saldos iniciais (auditoria inicial didática)",
norma="NBC TA 510 (R1) (NORMAS p. 497–520). Itens: 5 (ler as demonstrações mais recentes e o relatório do auditor antecessor), 6 (evidência sobre os saldos iniciais: (a) transportados corretamente; (b) políticas apropriadas; (c) revisão dos papéis do antecessor, procedimentos do período corrente ou procedimentos específicos), 7 (distorções nos saldos iniciais), 8 (consistência de políticas) — p. 499; 9–13 (conclusões e relatório, inclusive opinião modificada do antecessor) — p. 500.",
objetivo="Obter evidência de que os saldos de abertura de 01/01/2025 não contêm distorções que afetem de forma relevante as DF de 2025 e de que as políticas contábeis foram aplicadas de forma consistente. O trabalho é tratado como inicial para fins didáticos: o 'auditor antecessor' é a PwC, que auditou 2024.",
conta="Balanço patrimonial consolidado de 31/12/2024 (comparativo) e DRE de 2024; ativo financeiro da concessão de abertura de R$ 25.209.768 mil.",
afirmacoes="Existência, integridade, avaliação e apresentação dos saldos de abertura; consistência das políticas. Ligação com D-B04-01, cujo gatilho é reduzir a materialidade de execução se houver ajustes de abertura.",
populacao=f"DF24 CPFL.pdf (Drive, pasta 01): BP p. 34–35 (impressas 2–3), DRE p. 36/4, nota 1.3 p. 45/13, nota 2.1 p. 46/14, Relatório da Administração item 8 p. 27, parecer do Conselho Fiscal p. 138, declaração da diretoria p. 139. DF25: comparativos p. 34–36, nota 3.19–3.20 p. 57–58. Comparação de 61 linhas: {PLAN}, aba PT510_Abertura.",
procedimentos=[
 ("510-01", "Ler a DF24 e identificar o auditor antecessor, o tipo de opinião e a data do relatório (item 5)", "Realizado com evidência pública (indireta: o relatório do auditor não está no PDF do Drive)"),
 ("510-02", "Conciliar as 61 linhas do BP de 31/12/2024 publicado (DF24) com o comparativo da DF25, além de totais e DRE (item 6(a))", "Realizado com evidência pública"),
 ("510-03", "Verificar reapresentações, reclassificações e mudanças de política (itens 6(b) e 8)", "Realizado com evidência pública"),
 ("510-04", "Revisar os papéis de trabalho do auditor antecessor (item 6(c)(i))", "Planejado por falta de acesso (não ocorreu)"),
 ("510-05", "Procedimentos específicos sobre o ativo financeiro da concessão de abertura: base de remuneração homologada e laudo de VNR de 2024", "Planejado por falta de acesso"),
 ("510-06", "Usar procedimentos do período corrente como evidência sobre a abertura: movimentação da nota 11 e retrospectiva do VNR (PT 520/540)", "Realizado com evidência pública"),
],
corpo="""
**1. Auditor antecessor e opinião sobre 2024 (item 5)**

- A PwC (PricewaterhouseCoopers Auditores Independentes) foi contratada para auditar as DF de 2024 (DF24, Relatório da Administração, item 8, p. 27).
- O relatório do auditor **não consta** do PDF disponível no Drive. A existência de relatório **sem ressalvas**, datado de 26/02/2025, é indicada:
  - no parecer do Conselho Fiscal de 25/02/2025 (DF24 p. 138);
  - na declaração da diretoria de que "reviram, discutiram e concordam com as opiniões expressas no parecer da PwC" (p. 139).
- As DF24 foram autorizadas em 17/02/2025 (nota 2.1, p. 46/14). **Evidência indireta**: obter o relatório completo pela CVM/ENET (pendência no B12).

**2. Saldos transportados corretamente (item 6(a))**

| Comparação | Resultado |
|---|---|
| 61 linhas do BP consolidado de 31/12/2024 (DF24 p. 34–35 × DF25 p. 34–35) | **0 diferenças** |
| Totais publicados × soma das linhas | Diferenças de ±1 e ±2 só de soma (arredondamento, DF25 nota 2.4, p. 46) |
| Total do ativo e do passivo + PL: 77.129.194 | Idênticos |
| DRE 2024 (receita, lucro bruto, resultado do serviço, LAIR, lucro líquido, lucro dos controladores) | Idênticos |
| Ativo financeiro da concessão de abertura: 25.209.768 | Idêntico; movimentação de 2025 reexecutada no B02 (CC05) |

A única alteração é de **nome de rubrica**: "Mútuo entre coligadas, controladas e controladora" (DF24) passou a "Mútuo com partes relacionadas" (DF25), sem mudança de valor (2.485.694). É uma reclassificação de apresentação sem efeito.

**3. Políticas contábeis e reapresentações (itens 6(b) e 8)**

- A DF25 não menciona reapresentação de comparativos, e os valores coincidem com a DF24.
- As normas que entraram em vigor em 01/01/2025, incluindo as alterações da IAS 21 sobre conversibilidade de moedas, "não afetaram materialmente" as DF (nota 3.19, p. 57–58).
- A política do ativo financeiro da concessão (valor justo por meio do resultado, VNR + IPCA) é descrita da mesma forma (DF25 nota 3, p. 47; nota 4, p. 59).
- **Fato de 2024 relevante para 2025:** a DF24 informava a consulta pública da ANEEL sobre a renovação das concessões e "não há impactos" (DF24 nota 1.3, p. 45/13). Em 2025, os pedidos foram aprovados pela ANEEL (DF25 nota 1.3, p. 44/12). Trata-se de evolução de fato, não de mudança de política (ver PT 540).

**4. O que não foi possível fazer**

- Não houve acesso aos papéis de trabalho da PwC (item 6(c)(i)), nem ao cadastro, à base de remuneração e ao laudo de VNR de 2024 (510-05).
- Como compensação parcial, o período corrente fornece evidência sobre a abertura:
  - a movimentação da nota 11 parte de 25.209.768 e fecha com o BP;
  - o modelo de expectativa do VNR reproduz o ajuste de 2024 com desvio de −0,4% (PT 520).
""",
evidencias=f"DF24 p. 27, 34–36, 45–46, 138–139; DF25 p. 34–36, 44, 46, 47, 57–59, 68; {PLAN} (PT510_Abertura). Referências cruzadas: PT 320 (D-B04-01), PT 520, PT 540, PT 560.",
resultados="Saldos de abertura transportados sem diferença (61 linhas; totais e DRE idênticos). Sem reapresentação. Uma rubrica renomeada sem efeito de valor. Opinião do antecessor sobre 2024 indicada como sem ressalvas (evidência indireta). Nenhum ajuste de abertura: o gatilho de D-B04-01 não é acionado.",
conclusao="Com base nos documentos públicos, não há indício de distorção nos saldos de abertura nem de inconsistência de políticas. A evidência é limitada pela falta de acesso aos papéis do antecessor e ao relatório do auditor de 2024 em versão integral.",
limitacoes="Relatório do auditor de 2024 não disponível no PDF do Drive. Papéis do antecessor e dados regulatórios de abertura não acessados. BP de 2024 transcrito visualmente (imagens).",
))

# --------------------------------------------------------------------------- 520
PTS.append(dict(
codigo="PT 520", titulo="Procedimentos analíticos — avaliação de risco e substantivo sobre o ajuste a valor justo do ativo financeiro da concessão",
norma="NBC TA 520 (Res. CFC 1.221/2009; NORMAS p. 521–529). Itens: 5 (procedimento analítico substantivo: (a) adequação à afirmação; (b) confiabilidade dos dados; (c) expectativa suficientemente precisa; (d) diferença aceitável sem investigação), 6 (analítico perto do fim: revisão geral — Bloco 11), 7 (investigar flutuações: indagar e corroborar) — p. 525. Uso para avaliação de risco: NBC TA 315 (R2).",
objetivo="(1) Planejamento: identificar variações e relações que sinalizem riscos. (2) Substantivo: testar se o ajuste a valor justo (VNR) de 2025 do ativo financeiro da concessão (R$ 1.285.173 mil) é coerente com uma expectativa independente. (3) Revisão final: planejada para o Bloco 11.",
conta="Ativo financeiro da concessão e receita de atualização (notas 11, 26 e 34); indicadores consolidados de resultado, liquidez e endividamento.",
afirmacoes="Avaliação e exatidão do ajuste a valor justo (R01); ocorrência da receita correspondente (R04). Planejamento: R13 (mútuos), R17 (liquidez).",
populacao=f"DF25 p. 34–36, 39, 68, 101, 110–111; DFs individuais Paulista, RGE e Piratininga (notas 11); IPCA IBGE 2024 e 2025; {PLAN}, abas PT520_Planejamento e PT520_Substantivo_VNR.",
procedimentos=[
 ("520-01", "Analíticos de planejamento: variações 2025 × 2024 e 7 indicadores", "Realizado com evidência pública"),
 ("520-02", "Analítico substantivo: expectativa = saldo inicial × IPCA + transferências × IPCA/2, no consolidado e por distribuidora, com retrospectiva de 2024", "Realizado com evidência pública"),
 ("520-03", "Conciliar o ganho da nota 34 com a nota 11 (VNR − baixa da atualização), em 2025 e 2024", "Realizado com evidência pública"),
 ("520-04", "Investigar a diferença acima do limite: indagar a administração e obter o cálculo do VNR da CPFL Paulista (item 7)", "Planejado por falta de acesso"),
 ("520-05", "Revisão analítica final das DF (item 6)", "Realizado com evidência pública — revisão analítica final executada no Bloco 12"),
],
corpo="""
**1. Analíticos de avaliação de risco (planejamento; não são evidência substantiva)**

| Indicador | 2025 | 2024 | Leitura |
|---|---:|---:|---|
| Margem bruta | 31,8% | 31,8% | Estável |
| Margem do LAIR | 18,2% | 19,0% | Leve queda: despesa financeira +13,8% |
| Liquidez corrente | 0,93 | 0,95 | CCL negativo de 1.259.649 (nota 1.4, p. 44/12) → R17, PT 570 |
| Dívida bruta / PL | 1,24 | 1,32 | Dívida de 29.055.727 |
| Ativo financeiro da concessão / ativo total | 36,5% | 32,7% | Concentração crescente → R01 |
| Mútuo com partes relacionadas | 4.412.650 | 2.485.694 | **+77,5%** → R13, PT 550 |

**2. Analítico substantivo do VNR — desenho antes da comparação**

| Elemento (item 5) | Definição |
|---|---|
| Adequação | A política (nota 4, p. 59) diz que, entre revisões tarifárias, o valor é atualizado pelo IPCA. A relação é previsível e adequada a um analítico |
| Dados | Saldos e movimentação de DF auditadas; IPCA oficial do IBGE: 4,26% em 2025, igual à "taxa no período" da nota 34 e.2 (p. 111/79), e 4,83% em 2024 |
| Expectativa | Saldo inicial × IPCA + transferências do ativo contratual × IPCA/2, supondo transferências distribuídas ao longo do ano |
| Precisão | O modelo reproduz 2024 com −0,4% no consolidado; +0,05% na Paulista, −1,0% na RGE e −0,04% na Piratininga |
| Limite de investigação | 30% da materialidade de execução = R$ 91.027 mil (julgamento, risco significativo) |

**3. Resultado**

| Entidade (2025) | VNR registrado | Expectativa | Diferença |
|---|---:|---:|---:|
| Consolidado | 1.285.173 | 1.145.694 | **139.479 (+12,2%)** |
| CPFL Paulista | 635.251 | 484.800 | 150.451 |
| RGE | 469.006 | 496.590 | (27.584) |
| CPFL Piratininga | 171.723 | 149.849 | 21.874 |
| CPFL Santa Cruz (por diferença) | 9.193 | 14.455 | (5.262) |

A diferença consolidada **excede o limite** e precisa ser investigada (item 7). Ela se concentra na CPFL Paulista, que explica 108% da diferença líquida.

**4. Investigação com fontes públicas**

- **Documentado:** em 2025, a Paulista teve **reajuste anual (RTA)** em 29/04/2025 (REH nº 3.452), e não revisão periódica (DF25 nota 26.2, p. 101/69). Uma reavaliação da base em revisão tarifária, que explicaria um salto, **não está documentada** para 2025.
- **Hipóteses não comprovadas:**
  - ajustes da base de remuneração por fiscalização ou laudo complementar;
  - diferença de índice ou de defasagem no cálculo da Paulista;
  - efeito de adições e unitizações ao longo do ano diferente do suposto.
- **Corroboração necessária:** indagar a administração e obter o cálculo do VNR da Paulista (520-04, planejado). Até lá, a diferença fica **não explicada** e é levada ao PT 540 como possível indicador de viés.

**5. Conciliação nota 11 × nota 34 (exatidão)**

O ganho reconhecido de 1.172.082 (nota 34 c, p. 110/78) é igual ao VNR de 1.285.173 menos a baixa da atualização de 113.091 (nota 11, p. 68). Diferença zero. A mesma relação vale para 2024: 1.104.267 − 96.326 = 1.007.941.
""",
evidencias=f"DF25 p. 34–36, 39, 44, 59, 68, 101, 110–111; DFs individuais (pasta 06), notas 11; IBGE — IPCA 2025 e 2024; {PLAN}. Referências cruzadas: PT 315 (R01, R13, R17), PT 540, PT 550, PT 570.",
resultados="Diferença de R$ 139.479 mil (+12,2%) acima do limite de R$ 91.027 mil, concentrada na Paulista e não explicada por documentação pública. Modelo aderente em 2024. Conciliação nota 11 × nota 34 sem diferença nos dois anos. Indicadores de planejamento confirmam R01, R13 e R17.",
conclusao="O analítico substantivo não fornece, sozinho, evidência suficiente sobre o VNR de 2025: a diferença exige corroboração junto à administração (planejada). A diferença representa 34% da materialidade global e não leva, isoladamente, a concluir por distorção.",
limitacoes="A expectativa é aproximação didática, não o modelo da administração (base de remuneração item a item). Não houve indagação. O saldo da Santa Cruz foi derivado por diferença.",
))

# --------------------------------------------------------------------------- 540
PTS.append(dict(
codigo="PT 540", titulo="Auditoria de estimativas contábeis — valor justo do ativo financeiro da concessão (VNR)",
norma="NBC TA 540 (R2) (DOU 23/10/2019; NORMAS p. 548–599). Itens: 13 (entendimento), 14 (revisão retrospectiva; p. 553), 16–17 (riscos inerentes: incerteza, complexidade, subjetividade; risco significativo; p. 554), 18–21 (respostas), 22–27 (como a administração elaborou: métodos 23, premissas significativas 24, dados 25, incerteza e divulgação 26; p. 555–556), 28–29 (estimativa pontual ou intervalo do auditor), 32 (indicadores de viés; p. 557), 33–36 (avaliação geral e razoabilidade; p. 558), 37 (representações).",
objetivo="Avaliar se o valor justo do ativo financeiro da concessão (R$ 29.623.619 mil; ajuste de 2025 de R$ 1.285.173 mil) e as divulgações relacionadas são razoáveis, considerando método, premissas, dados, incerteza, possível viés e a renovação das concessões.",
conta="Ativo financeiro da concessão (nota 11, p. 68), mensurado a valor justo de nível 3 (nota 3, p. 47; nota 4, p. 59; nota 34); receita de atualização (nota 26).",
afirmacoes="Avaliação, classificação e divulgação. Risco significativo R01 e PAA 3 da PwC (DF25 p. 29); R18 (renovação); R16 (viés da administração).",
populacao=f"DF25 p. 29, 44, 47, 59, 68, 101, 110–111; DFs individuais (notas 11); ITR 2T26 nota 1.2 (p. 43/9) e nota 11 (p. 49/15); Fato Relevante de 08/05/2026; {PLAN}, aba PT540_Sensibilidade.",
procedimentos=[
 ("540-01", "Entender o método, as premissas e os dados da administração e avaliar os riscos inerentes (itens 13 e 16)", "Realizado com evidência pública"),
 ("540-02", "Revisão retrospectiva: VNR de 2024 e 2025 × modelo de IPCA (item 14)", "Realizado com evidência pública"),
 ("540-03", "Testar a premissa de IPCA contra fonte oficial (item 24)", "Realizado com evidência pública"),
 ("540-04", "Sensibilidade reproduzível (IPCA ±0,5/±1 p.p.; base homologada ±2%/±5%) e reprodução da sensibilidade divulgada", "Realizado com evidência pública (aproximação)"),
 ("540-05", "Testar a base de remuneração homologada, o cadastro e o laudo de VNR (itens 23 e 25); desenvolver estimativa pontual ou intervalo (item 28)", "Planejado por falta de acesso"),
 ("540-06", "Avaliar indicadores de viés (item 32) e a divulgação da incerteza e da renovação (itens 26 e 36)", "Realizado com evidência pública"),
 ("540-07", "Testes de existência e avaliação no cadastro (simulação)", "Simulado para fins didáticos (PT 530)"),
],
corpo="""
**1. A estimativa e seus riscos inerentes (itens 13 e 16)**

O direito de indenização ao fim da concessão é mensurado a valor justo de nível 3:

- **Ponto de partida:** a base de remuneração avaliada a VNR na revisão tarifária, a cada 4 ou 5 anos, homologada pela ANEEL.
- **Entre revisões:** atualização pelo IPCA (nota 4, p. 59; nota 34, p. 110/78).

| Fator de risco inerente | Avaliação |
|---|---|
| Incerteza de estimativa | Alta. Depende da base homologada (não divulgada) e do prazo da concessão |
| Complexidade | Alta. Metodologia regulatória e cadastro de milhões de itens |
| Subjetividade | Moderada. Unitização, baixas e classificação entre ativo financeiro, ativo contratual e intangível |
| **Conclusão** | Risco significativo (R01), coerente com o PAA 3 da PwC (DF25 p. 29) |

**2. Premissas, dados e método (itens 23–25)**

- **IPCA:** a taxa de 4,26% de 2025 coincide com o IPCA oficial do IBGE e com a "taxa no período" da nota 34 e.2 (p. 111/79). Premissa observável, testada.
- **Base homologada (VNR/BRR) e cadastro:** não divulgados. **Não testáveis** com evidência pública (540-05, planejado). O PT 530 demonstra, em ambiente simulado, os testes que seriam feitos no cadastro.
- **Método:** coerente com a regulação descrita, e igual ao de 2024 (DF24 e DF25).

**3. Revisão retrospectiva (item 14)**

O modelo de IPCA reproduz o ajuste de 2024 (diferença de −0,4%), mas não o de 2025 (+12,2%, ou +R$ 139.479 mil). A diferença se concentra na CPFL Paulista, que em 2025 teve apenas reajuste anual (PT 520).

**4. Sensibilidade (aproximação didática, não recálculo do modelo da administração)**

| Cenário | Efeito (R$ mil) | % da materialidade global |
|---|---:|---:|
| IPCA ±0,5 p.p. | ±134.471 | ±33% |
| IPCA ±1,0 p.p. | ±268.942 | ±66% |
| Base homologada ±2% | ±592.472 | ±146% |
| Base homologada ±5% | ±1.481.181 | ±366% |

A base de cálculo é o saldo inicial mais metade das transferências (26.894.226) para o IPCA, e o saldo final (29.623.619) para a base homologada.

A **sensibilidade divulgada** pela companhia (nota 34 e.2, p. 111/79) foi reproduzida com diferença menor que R$ 1 mil. Exposição ativa ao IPCA de 29.653.297 × 9,63% = 2.855.613 no cenário provável; reduções de 25% e 50% do índice.

**Leitura:** a variação de poucos pontos percentuais na base homologada supera a materialidade global. É a incerteza que justifica o risco significativo, e não um indicativo de erro.

**5. Estimativa do auditor (item 28)**

**Não foi desenvolvida** estimativa pontual nem intervalo. Faltam os dados indispensáveis: a base homologada por distribuidora e a data-base de cada laudo. A expectativa do PT 520 serve como analítico, **não** como recálculo exato.

**6. Indicadores de viés (item 32)**

- **Indicador:** a diferença de 2025 aumenta o ativo e a receita na mesma direção (+12,2% sobre o modelo), sem explicação documentada.
- **Contraindicadores:**
  - aderência em 2024;
  - RGE e Santa Cruz abaixo da expectativa em 2025;
  - mesma metodologia nos dois anos.
- **Conclusão:** é um indicador isolado, **não conclusivo**. Será considerado com o PT 240 (R16) e com as representações (PT 580, item 37).

**7. Renovação das concessões: incerteza, divulgação e evento posterior**

- **Em 31/12/2025:**
  - a ANEEL havia aprovado os pedidos de prorrogação por 30 anos da RGE (março), da Piratininga (junho) e da Paulista (novembro de 2025);
  - a decisão final cabia ao MME (DF25 nota 1.3, p. 44/12);
  - os contratos vigentes previam indenização ao fim do prazo (2027/2028), base da classificação como ativo financeiro.
- **Depois da emissão das DF (04/03/2026):**
  - despacho do MME no DOU de 06/04/2026;
  - assinatura dos aditivos em 06/05/2026 (ITR 2T26 nota 1.2, p. 43/9; Fato Relevante de 08/05/2026);
  - reclassificação prospectiva de **R$ 29.599.494 mil** do ativo financeiro da concessão para o intangível: Paulista 12.737.816; Piratininga 3.686.631; RGE 13.175.047 (ITR 2T26 nota 11, p. 49/15). Isso equivale a 99,9% do saldo de 31/12/2025.
- **Avaliação (itens 26 e 36):**
  - A companhia tratou a assinatura como **novo evento contratual**, com efeito prospectivo em 2026. Isso é coerente com o fato de os aditivos não estarem assinados em 31/12/2025. A classificação em 2025 não parece afetada.
  - A **divulgação** da nota 1.3 informa o andamento, mas **não quantifica** o efeito possível na classificação nem a incerteza sobre o prazo da indenização.
  - Em auditoria real, discutir com a administração e a governança se a divulgação da incerteza de estimativa é suficiente (item 36; PT 260). Momento do fato: PT 560 (Bloco 10).
""",
evidencias=f"DF25 p. 29, 44, 47, 59, 68, 101, 110–111; DF24 nota 1.3 p. 45/13; DFs individuais (notas 11); ITR 2T26 p. 43 e 49; Fato Relevante de 08/05/2026; IBGE (IPCA); {PLAN} (PT540_Sensibilidade, PT520_Substantivo_VNR). Referências cruzadas: PT 240 (R16), PT 315 (R01, R18), PT 520, PT 530, PT 560, PT 580.",
resultados="Premissa de IPCA confirmada. Base homologada não testável. Retrospectiva de 2024 aderente e de 2025 com desvio não explicado de +12,2% (Paulista). Sensibilidade: ±1 p.p. de IPCA = ±66% da materialidade global; ±2% na base homologada = ±146%. Sensibilidade divulgada reproduzida. Renovação: reclassificação de 99,9% do saldo em 2026, como evento novo. Divulgação de 2025 sem quantificação do efeito possível.",
conclusao="Com evidência pública, a estimativa é coerente na premissa observável (IPCA) e no método. A razoabilidade do saldo não pode ser concluída sem a base homologada e a explicação do desvio da Paulista (procedimentos planejados). O ponto de divulgação sobre a renovação deve ser levado à governança. Não é opinião sobre a CPFL.",
limitacoes="Sem acesso ao modelo, à base de remuneração, aos laudos e à administração. Cenários são aproximações identificadas como tais. A taxa do 'cenário provável' de IPCA (9,63%) é da companhia e não foi conferida em fonte externa.",
))

# --------------------------------------------------------------------------- 550
PTS.append(dict(
codigo="PT 550", titulo="Partes relacionadas",
norma="NBC TA 550 (Res. CFC 1.224/2009; NORMAS p. 600–624). Itens: 11–14 (entendimento: discussão da equipe, indagações, controles; p. 606), 15–17 (alerta para relações e transações não divulgadas; p. 607), 18–19 (riscos; fatores de fraude), 20–22 (respostas; relações não identificadas antes; p. 608), 23 (transações significativas fora do curso normal), 24 (afirmação de condições equivalentes às de mercado; p. 609), 25–26 (avaliação), 27 (comunicação), 28 (documentação; p. 610).",
objetivo="Mapear partes relacionadas, vínculos, saldos, transações e divulgações; identificar a origem de cada dado; avaliar transações significativas; e planejar a busca de relações ou operações não divulgadas.",
conta="Mútuos com partes relacionadas (PC 19.416 + PNC 4.393.234 = 4.412.650; BP p. 35/3); debêntures detidas pelo controlador; compras de energia; remuneração do pessoal-chave (nota 31, p. 103–104/71–72).",
afirmacoes="Integridade (relações e transações não identificadas), apresentação e divulgação, ocorrência. Risco R13 (moderado); fatores de fraude ligados ao controlador (PT 240).",
populacao=f"DF25 nota 31 (p. 103–104/71–72), nota 1, BP p. 35; Política de Partes Relacionadas (CA de 16/12/2021, Drive pasta 03); Estatuto Social (art. 17, alínea n, citado pela Política; não lido neste bloco); {PLAN}, aba PT550_PartesRel.",
procedimentos=[
 ("550-01", "Mapear partes relacionadas e vínculos divulgados (controladores, controle comum, controle conjunto, entidades sem fins lucrativos, planos de previdência, pessoal-chave)", "Realizado com evidência pública"),
 ("550-02", "Transcrever saldos e transações por natureza (2025 e 2024) e conciliar os mútuos com o BP", "Realizado com evidência pública"),
 ("550-03", "Avaliar transações significativas: mútuo com a SGEL (4.412.650), liquidação antecipada dos mútuos com a SGBP e debêntures detidas pela SGBP (item 23)", "Realizado com evidência pública (parcial)"),
 ("550-04", "Ler a política e o fluxo de aprovação (Comitê de Partes Relacionadas; Conselho de Administração para montante significativo)", "Realizado com evidência pública"),
 ("550-05", "Busca de completude: atas do CA e do Comitê, FR seção de partes relacionadas (truncada no Drive), comunicados de transações com partes relacionadas na CVM, contratos de mútuo, cadastro de fornecedores × lista de partes relacionadas", "Planejado por falta de acesso"),
 ("550-06", "Indagar a administração e a governança e obter representações (itens 13 e 26; PT 580)", "Planejado por falta de acesso"),
],
corpo="""
**1. Partes relacionadas identificadas e origem do dado**

| Parte | Vínculo | Origem |
|---|---|---|
| State Grid Corporation of China | Controladora final (estatal chinesa) | Nota 31, p. 103/71 |
| State Grid Brazil Power Participações S.A. (SGBP) | Acionista controlador | Nota 31, p. 103/71 |
| ESC Energia S.A. | Acionista controlador, controlada pela SGBP | Nota 31, p. 103/71 |
| State Grid Europe Limited (SGEL) | Entidade sob controle comum; credora dos mútuos de 2025 | Nota 31 c), p. 104/72 |
| Empreendimentos controlados em conjunto (BAESA, Chapecoense e outros) | Controle conjunto | Nota 31 tabela; nota 13 (PT 600) |
| Instituto CPFL | Entidade ligada ao grupo | Nota 31 tabela |
| Vivest e Família Previdência | Planos de benefício pós-emprego | Nota 31 (remissão à nota 20) |
| Pessoal-chave da administração | Remuneração de 80.523 (80.597 em 2024) | Nota 31, p. 104/72 |

**A lista divulgada não comprova completude** (item 15). Ela é o ponto de partida da busca planejada (550-05).

**2. Saldos e transações (R$ mil, consolidado)**

| Natureza | Passivo 2025 | Passivo 2024 | Despesa 2025 | Despesa 2024 |
|---|---:|---:|---:|---:|
| Mútuo — SGEL (controle comum) | 4.412.650 | — | (41.667) | — |
| Mútuo — SGBP | — | 2.485.694 | (368.077) | (311.573) |
| Outras operações financeiras — SGBP (debêntures da Paulista) | 325.563 | 1.507.938 | (97.450) | (177.955) |
| Energia — controle comum | — | — | (424.459) | (410.890) |
| Energia — controlados em conjunto e outros | 76.888 | 104.378 | (897.183) | (965.058) |

O mútuo total da nota 31 (4.412.650) concilia com o BP (PC 19.416 + PNC 4.393.234), com diferença zero, e cresceu 77,5% sobre 2024. As despesas totais com partes relacionadas são de cerca de R$ 1,86 bilhão (aba PT550).

**3. Transações significativas (item 23)**

- **Mútuo com a SGEL:**
  - **Contraparte e termos:** contratos das controladas Paulista, Piratininga, RGE, Santa Cruz e CPFL Brasil com a SGEL; vencimento em setembro de 2028; juros semestrais a partir de março de 2026; remuneração em renminbi + 1,98%, com derivativos para CDI − 0,365%.
  - **Contexto:** substituiu os mútuos com a SGBP (CDI + 1,1%), liquidados antecipadamente em dezembro de 2025 (nota 31 c, p. 104/72).
  - **Exposição cambial em renminbi:** 4.958.307 (nota 34 e.1, p. 111/79), protegida por swap.
- **Debêntures da Paulista detidas pela SGBP:** CDI + 0,59%, vencimento a partir de fevereiro de 2029 (nota 31 d). O saldo caiu de 1.507.938 para 325.563.
- **Avaliação:** a companhia afirma condições "semelhantes às de mercado" para o mercado livre de energia (nota 31 a). Para os mútuos e as debêntures, a **comparação com taxas de mercado** (item 24), a **razão negocial** e a **aprovação** pela política ficam planejadas (550-05/06). O custo efetivo em CDI do mútuo com a SGEL (CDI − 0,365%) é inferior ao do mútuo anterior (CDI + 1,1%). É uma indicação de condição favorável, não verificada.

**4. Governança e política**

- A Política de Partes Relacionadas (aprovada pelo CA em 16/12/2021) estabelece:
  - transações em condições de mercado (cap. V);
  - lista de partes relacionadas mantida pela Diretoria de Governança Corporativa (V.3);
  - aprovação de transações de "montante significativo" pelo Conselho, com manifestação prévia do Comitê de Partes Relacionadas (V.4);
  - divulgação no Formulário de Referência e por comunicado ao mercado (cap. VIII).
- A nota 31 confirma o comitê: dois independentes e um executivo (p. 104/72).
- **Controle relevante para o auditor:** a existência e a atualização da lista e as atas que aprovaram o mútuo com a SGEL. Não verificados (550-05).

**5. Busca de relações não divulgadas (item 15): plano**

1. Atas do Conselho, do Comitê de Partes Relacionadas e do Comitê de Auditoria de 2025 e 2026.
2. Formulário de Referência íntegro, seção de partes relacionadas (o arquivo do Drive está truncado; PB02-03).
3. Comunicados de transações com partes relacionadas na CVM.
4. Contratos de mútuo e de debêntures.
5. Cruzamento do cadastro de fornecedores e clientes com a lista de partes relacionadas.
6. Confirmação externa dos saldos com a SGEL e a SGBP (PT 505, modelo não enviado).
""",
evidencias=f"DF25 nota 31 (p. 103–104), BP p. 35, nota 34 e.1 (p. 111); Política de Partes Relacionadas (Drive pasta 03); {PLAN} (PT550_PartesRel). Referências cruzadas: PT 240, PT 315 (R13), PT 505, PT 580, PT 600.",
resultados="Oito categorias de partes relacionadas mapeadas com origem. Mútuo de 4.412.650 conciliado com o BP. Substituição dos mútuos da SGBP pelo mútuo da SGEL e redução das debêntures detidas pela SGBP identificadas como transações significativas. Completude e condições de mercado não verificadas.",
conclusao="As divulgações da nota 31 são internamente consistentes com o BP. A avaliação de completude e das condições dos mútuos com o grupo controlador depende de procedimentos planejados. R13 permanece moderado.",
limitacoes="Sem acesso a atas, contratos, lista interna de partes relacionadas e FR íntegro. Sem indagações nem confirmações.",
))

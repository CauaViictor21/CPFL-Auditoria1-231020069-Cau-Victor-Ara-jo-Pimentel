# -*- coding: utf-8 -*-
"""PTs do Bloco 11: PT 260, PT 265, PT 580; fechamento dos PTs 450 e 500 (UPDATES) e conclusão integrada."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "23/10/2026"
PLAN = "CPFL_B11_Comunicacoes_Distorcoes_Evidencia.xlsx"
MIN = "CPFL_B11_Minutas_Governanca_Representacoes_NAO_ENVIADAS (PDF/DOCX)"
PTS = []

# --------------------------------------------------------------------------- 260
PTS.append(dict(
codigo="PT 260", titulo="Comunicação com os responsáveis pela governança (MINUTA NÃO ENVIADA)",
norma="NBC TA 260 (R2) (DOU 04/07/2016; NORMAS p. 203–224). Itens: 9 (objetivos; p. 205), 11–13 (identificar os responsáveis pela governança; comunicação com subgrupo ou comitê; p. 206), 14 (responsabilidades do auditor), 15 (alcance e época planejados), 16 (constatações significativas: (a) aspectos qualitativos das práticas contábeis, (b) dificuldades significativas, (c) assuntos discutidos com a administração, (d) representações solicitadas, (e) outros assuntos), 17 (independência, entidades listadas; p. 207), 18 (processo de comunicação), 19 (forma escrita das constatações significativas), 21 (tempestividade), 22 (adequação do processo; p. 208), 23 (documentação). Apoio: NBC TA 265 item 9; NBC TA 450 itens 12–13.",
objetivo="Definir a quem, o que, quando e como seriam comunicados os assuntos exigidos pela norma, e preparar a minuta da comunicação escrita. Nada foi enviado.",
conta="Processo de comunicação do trabalho como um todo (planejamento e constatações).",
afirmacoes="Não se aplica a afirmações. Riscos: comunicação incompleta ou intempestiva; comunicar como fato o que é simulação ou hipótese; falta de independência não divulgada.",
populacao=f"Conclusões dos PTs 200 a 600; {PLAN}, aba PT260_Checklist; {MIN}, seção 1. Estrutura de governança: Conselho de Administração (aprovou a emissão das DF em 04/03/2026, DF25 p. 32) e o órgão de supervisão do processo de relatório financeiro indicado no Formulário de Referência (seção 12 truncada no arquivo disponível, DV15).",
procedimentos=[
 ("260-01", "Identificar os responsáveis pela governança e o subgrupo apropriado (itens 11–13)", "Realizado com evidência pública (parcial: FR truncado)"),
 ("260-02", "Listar os assuntos dos itens 14–17 e mapear a origem de cada um nos PTs", "Realizado com evidência pública (documental)"),
 ("260-03", "Redigir minuta da comunicação escrita das constatações significativas (item 19)", "Simulado para fins didáticos — MINUTA NÃO ENVIADA"),
 ("260-04", "Comunicar o alcance e a época planejados antes da execução (itens 15 e 21)", "Planejado por falta de acesso"),
 ("260-05", "Avaliar a adequação da comunicação recíproca (item 22)", "Planejado por falta de acesso"),
],
corpo="""
**1. Responsáveis pela governança (itens 11–13)**

- O Conselho de Administração aprovou a emissão das DF de 2025 em 04/03/2026, mesma data do relatório da PwC (DF25 p. 32).
- A composição de comitês e do conselho fiscal estaria na seção 12 do Formulário de Referência, mas o arquivo disponível está truncado (DV15). Na auditoria real, a comunicação iria ao subgrupo com responsabilidade pela supervisão do relatório financeiro, e o auditor avaliaria se também precisa comunicar ao conselho inteiro (item 13).
- Não há nomes de pessoas neste PT.

**2. Assuntos e situação neste exercício (itens 14–17)**

| Item | Assunto | Conteúdo que seria comunicado | Origem |
|---|---|---|---|
| 14 | Responsabilidades do auditor | Exame segundo as NBC TA; a auditoria não exime a administração | PT 200/210 |
| 15 | Alcance e época | Consolidado; materialidade global 404.562; riscos significativos R01, R02, R03 e R16; uso de base sintética no R01 | PT 300/315/320 |
| 16(a) | Práticas contábeis | VNR do ativo financeiro (nível 3; IPCA ±1 p.p. = ±66% da global); divulgação da renovação sem quantificação do efeito possível; julgamento de controle conjunto | PT 540/600 |
| 16(b) | Dificuldades significativas | Sem acesso a registros, pessoas e terceiros; FR truncado; relatório de 2024 ausente do PDF | PT 500/510 |
| 16(c) | Assuntos com a administração | Nenhuma discussão ocorreu. Seriam: diferença de +150 mil no VNR da Paulista; reconhecimento do IRRF Jantus (139.291) | PT 520/560 |
| 16(d) | Representações solicitadas | Minuta do PT 580 (não enviada) | PT 580 |
| 16(e) | Outros assuntos | Mútuo SGEL 4.412.650 (parte relacionada); CCL negativo de 1.259.649 | PT 550/570 |
| 17 | Independência | Declaração do aluno: sem vínculo com o Grupo CPFL; nenhum serviço prestado | PT 200 |
| 265 item 9 | Deficiências significativas | Nenhuma identificada com evidência pública | PT 265 |
| 450 item 12 | Distorções não corrigidas | Nenhuma distorção real; as sintéticas são apenas resultado didático | PT 450 |

**3. Forma e época (itens 18–22)**

- Escrita para as constatações significativas (item 19). Oral, com registro, para o planejamento (item 15).
- Planejamento: antes da execução dos testes. Constatações: antes da data do relatório. Independência: na conclusão.
- **Separação obrigatória na minuta:** (i) fatos com evidência pública; (ii) hipóteses que dependem de acesso; (iii) resultados sintéticos. A minuta não apresenta a simulação como achado sobre a CPFL.

A minuta completa está em {MIN}, seção 1.
""".replace("{MIN}", MIN),
evidencias=f"NORMAS p. 203–208; DF25 p. 32; {PLAN} (PT260_Checklist); {MIN}. Referências cruzadas: PT 200, PT 265, PT 315, PT 320, PT 450, PT 520, PT 540, PT 550, PT 560, PT 570, PT 580.",
resultados="Dez assuntos mapeados com origem. Nenhum assunto do item 16(c) foi efetivamente discutido. Minuta preparada e NÃO ENVIADA.",
conclusao="O conteúdo exigido pela NBC TA 260 está identificado e rastreável aos PTs. A comunicação recíproca, que é o propósito da norma, não ocorreu. Não é conclusão sobre a governança da CPFL.",
limitacoes="Sem contato com a governança. Estrutura de comitês não confirmada (FR truncado). A adequação da comunicação recíproca (item 22) não pode ser avaliada.",
))

# --------------------------------------------------------------------------- 265
PTS.append(dict(
codigo="PT 265", titulo="Comunicação de deficiências de controle interno",
norma="NBC TA 265 (Res. CFC 1.210/09; NORMAS p. 225–234). Itens: 5 (objetivo; p. 228), 6 (definições: deficiência e deficiência significativa; p. 229), 7 (determinar se há deficiências), 8 (determinar se são significativas), 9 (comunicar por escrito à governança, tempestivamente), 10 (comunicar à administração; p. 229), 11 (conteúdo da comunicação escrita; p. 230); A5–A7 (indicadores de deficiência significativa).",
objetivo="Avaliar se as condições encontradas indicam deficiências de controle interno da CPFL e, se significativas, como seriam comunicadas. Separar deficiências reais, hipóteses dependentes de acesso e achados sintéticos. A falta de acesso do aluno não é tratada como deficiência da companhia.",
conta="Controles relevantes para os riscos R01 (cadastro e VNR), R03 (medição e faturamento), R07 (contencioso), R13 (partes relacionadas) e R16 (lançamentos manuais).",
afirmacoes="Riscos de controle associados a existência, avaliação, integridade e divulgação.",
populacao=f"{PLAN}, aba PT265_Matriz (DC-01 a DC-06); PTs 315, 330, 450, 520, 530, 540, 560.",
procedimentos=[
 ("265-01", "Construir a matriz condição/critério/causa/efeito/recomendação/evidência (itens 7–8)", "Realizado com evidência pública (DC-02 a DC-06) / Simulado (DC-01)"),
 ("265-02", "Classificar cada condição: real, hipótese, sintética ou do preparador", "Realizado com evidência pública (documental)"),
 ("265-03", "Avaliar significância com os indicadores A5–A7", "Realizado com evidência pública (limitado)"),
 ("265-04", "Testar controles para confirmar deficiências (NBC TA 330 item 8)", "Planejado por falta de acesso"),
 ("265-05", "Comunicar por escrito à governança e à administração (itens 9–11)", "Simulado para fins didáticos — MINUTA NÃO ENVIADA"),
],
corpo="""
**1. Matriz resumida (detalhe na aba PT265_Matriz)**

| Ref. | Categoria | Condição | Classificação |
|---|---|---|---|
| DC-01 | **Sintética** | Duplicidades, baixados com valor, valores fora do recálculo e categorias incoerentes na base simulada | Seria significativa num caso real; **não é deficiência da CPFL** |
| DC-02 | Hipótese | VNR da Paulista +150.451 acima da expectativa, sem explicação pública | Não avaliável sem acesso |
| DC-03 | Hipótese | Reconhecimento do IRRF Jantus (139.291) não demonstrado nas notas (DF25 p. 96) | Não avaliável sem acesso |
| DC-04 | Real (divulgação) | Nota 1.3 (p. 44) sem quantificar o efeito possível da renovação; em 2026, 29.599.494 foram reclassificados (ITR 2T26 p. 49) | Ponto de divulgação, **não** deficiência de controle |
| DC-05 | Falta de acesso | Controles de TI, medição e faturamento não testados | **Não é deficiência da companhia** |
| DC-06 | Preparador | Erros de transcrição corrigidos (Apêndice A) | Qualidade do trabalho (PT 220) |

**2. Avaliação de significância (item 8 e A5–A7)**

- Uma deficiência exige saber que um controle falta ou falhou. Sem testes de controles, só há **indícios** (DC-02, DC-03), e eles podem ter explicação legítima.
- A opinião sem modificação da PwC e a ausência de PAA sobre controles (DF25 p. 26–32) não provam a eficácia dos controles. Também não indicam deficiência.
- **Conclusão do item 8:** nenhuma deficiência significativa da CPFL foi identificada com evidência pública.

**3. Comunicação (itens 9–11)**

- Sem deficiência significativa, não há comunicação obrigatória à governança pelo item 9.
- A minuta do item 11 está em {MIN}, seção 2. Ela comunica DC-01 apenas como demonstração didática, com a ressalva de que é sintética, e lista DC-02 e DC-03 como assuntos a investigar, não como deficiências.
""".replace("{MIN}", MIN),
evidencias=f"NORMAS p. 228–230; DF25 p. 26–32, 44, 96; ITR 2T26 p. 49; {PLAN} (PT265_Matriz); {MIN}. Referências cruzadas: PT 220, PT 260, PT 315, PT 330, PT 450, PT 520, PT 530, PT 540, PT 560.",
resultados="Seis condições avaliadas: 1 sintética, 2 hipóteses, 1 ponto de divulgação, 1 limitação de acesso e 1 erro do preparador. Nenhuma deficiência significativa real.",
conclusao="Com a evidência pública, não há base para afirmar deficiência significativa de controle interno da CPFL. Isso não é afirmação de que os controles são eficazes. Não é conclusão sobre a CPFL.",
limitacoes="Nenhum controle foi testado. A classificação depende de procedimentos planejados (PT 330).",
))

# --------------------------------------------------------------------------- 580
PTS.append(dict(
codigo="PT 580", titulo="Representações formais — minuta de carta (NÃO ENVIADA, sem assinatura)",
norma="NBC TA 580 (R1) (DOU 05/09/2016; NORMAS p. 660–671). Itens: 6 (objetivos; p. 662), 9 (a quem solicitar; p. 663), 10 (elaboração das DF), 11 (informações fornecidas e integridade das transações; p. 663–664), 13 (outras representações exigidas por outras NBC TA ou julgadas necessárias), 14 (data: o mais próxima possível, mas não posterior à do relatório), 15 (forma de carta; p. 664), 16–18 (dúvidas sobre a confiabilidade e inconsistências), 19–20 (representações não fornecidas: efeito na opinião; p. 665). Representações exigidas por outras normas: NBC TA 240, 250, 450 (item 14), 501 (item 12), 540, 550, 560 (item 9), 570.",
objetivo="Preparar a minuta da carta de representação que seria solicitada à administração, incluindo as representações específicas exigidas por outras NBC TA e as ligadas aos riscos do trabalho. Nada foi enviado e nada foi assinado.",
conta="DF consolidadas e individuais de 31/12/2025 como um todo.",
afirmacoes="Todas. Representações não substituem evidência (A1).",
populacao=f"{MIN}, seção 3; riscos R01–R19 (PT 315); PTs 240, 250, 450, 501, 540, 550, 560 e 570.",
procedimentos=[
 ("580-01", "Definir a quem solicitar: diretor-presidente e diretor financeiro, por categoria (item 9)", "Realizado com evidência pública (documental)"),
 ("580-02", "Redigir as representações gerais (itens 10–11) e específicas (item 13)", "Simulado para fins didáticos — MINUTA NÃO ENVIADA"),
 ("580-03", "Definir a data e a forma (itens 14–15)", "Realizado com evidência pública (documental): data em branco"),
 ("580-04", "Obter a carta assinada e avaliar sua confiabilidade (itens 16–18)", "Planejado por falta de acesso"),
 ("580-05", "Tratar recusa ou representação não confiável (itens 19–20)", "Planejado por falta de acesso"),
],
corpo="""
**1. Destinatários e data**

- Signatários: **diretor-presidente e diretor financeiro** (categoria), sem nomes. Campos de assinatura em branco.
- Data: **em branco**. A regra (item 14) é a data mais próxima possível do relatório do auditor, nunca posterior. Como este trabalho não emite relatório, não se inventa data.

**2. Conteúdo da minuta**

| Grupo | Representação | Norma / risco |
|---|---|---|
| Gerais | Responsabilidade pela elaboração das DF segundo as práticas contábeis adotadas no Brasil e as IFRS | 580 item 10 |
| Gerais | Acesso a todas as informações e registros; todas as transações registradas | 580 item 11 |
| Fraude | Responsabilidade pelos controles de prevenção; resultado da avaliação de risco; conhecimento de fraude ou suspeita | 240 / R16 |
| Leis | Descumprimentos conhecidos de leis e da regulação da ANEEL | 250 |
| Distorções | Efeito das distorções não corrigidas imaterial, com relação anexa | 450 item 14 |
| Litígios | Todos os litígios conhecidos informados e avaliados; **IRRF Jantus registrado em 31/12/2025** | 501 item 12 / R07 |
| Estimativas | Métodos, premissas e dados razoáveis, inclusive o VNR (IPCA e base de remuneração) e a explicação da variação da Paulista | 540 / R01 |
| Renovação | Divulgação adequada dos efeitos esperados dos aditivos de concessão | 540 / CPC 26 |
| Partes relacionadas | Identidade das partes e todas as transações informadas, inclusive o mútuo SGEL | 550 / R13 |
| Eventos subsequentes | Todos os eventos até a data da carta ajustados ou divulgados | 560 item 9 |
| Continuidade | Planos para os vencimentos de curto prazo; ausência de descumprimento de covenants | 570 / R17 |

**3. Se a carta não fosse fornecida (itens 19–20)**

A recusa das representações dos itens 10 e 11 levaria à abstenção de opinião. Neste trabalho a situação não se aplica, porque não há opinião.

Minuta completa: {MIN}, seção 3.
""".replace("{MIN}", MIN),
evidencias=f"NORMAS p. 662–665; {MIN}; PT 315 (R01, R07, R13, R16, R17). Referências cruzadas: PT 240, PT 250, PT 450, PT 501, PT 540, PT 550, PT 560, PT 570.",
resultados="Minuta com 11 grupos de representação, incluindo as específicas exigidas por outras normas. Sem assinatura, sem data e NÃO ENVIADA.",
conclusao="A minuta cobre as representações exigidas e as ligadas aos riscos significativos. Não foi obtida representação alguma, então nenhum procedimento se apoia nela.",
limitacoes="Sem administração para assinar. Representações não substituem evidência (A1).",
))

# --------------------------------------------------------------------------- fechamento 450 e 500
ADD_450 = """
**5. Fechamento em 23/10/2026 (Bloco 11): consolidação com os demais PTs (itens 10–11)**

Distorções e divergências por origem (detalhe na aba PT450_Consolidado da planilha B11):

| Origem | Itens | Valor (R$ mil) | Tratamento |
|---|---|---:|---|
| **Real, sustentada por evidência pública** | Nenhuma | 0 | Nada a acumular |
| **Sintética** | DS-01 a DS-05 | 117.484 líquido (124.296 bruto) | Acumulada só na simulação; igual ao PT 530 |
| **Hipótese dependente de acesso** | DH-01 IRRF Jantus (139.291); DH-02 VNR acima da expectativa (139.479) | — | **Não acumuladas**: não há base para afirmar distorção |
| **Qualitativa** | DQ-01 divulgação da renovação (nota 1.3) | — | Assunto para a governança (PT 260) |
| **Do preparador** | DX-01 transcrição (DV01, DV11–DV13, DV17, DV18); DX-02 arredondamento | — | Excluídas: não são da companhia |

- **Sem dupla contagem.** As exceções do MUS não são somadas às dos testes integrais, porque são os mesmos registros. A UML residual é risco de amostragem e não entra na soma.
- **Hipóteses somadas** (DH-01 + DH-02 = 278.770 = 92% da execução e 69% da global) ficam abaixo da global mesmo no pior caso. Ainda assim, são o principal risco remanescente, e a conclusão depende de investigá-las.
- **Materialidade (item 10):** não revista. Os referenciais (DF25 p. 34–36) não mudaram.
- **Relevância individual e em conjunto (item 11):** nenhuma distorção real; a simulada não é relevante frente à global (29,0%).
- **Representação (item 14):** prevista na minuta do PT 580.
"""
ADD_500 = """
**8. Fechamento em 23/10/2026 (Bloco 11): suficiência e adequação por risco e afirmação (itens 6–11)**

Matriz completa: aba PT500_Matriz da planilha B11. Escala: S = suficiente para a conclusão limitada deste exercício; P = parcial; I = insuficiente.

| Risco / área | Afirmações | Evidência principal | Suficiência | Lacuna |
|---|---|---|---|---|
| R01 Ativo financeiro | Avaliação, classificação | Movimentação, saldos por distribuidora, analítico, sensibilidade, renovação, base sintética | P | Base homologada, laudo, cadastro real |
| R02 Ativo contratual | Avaliação | Saldos e PAA da PwC | I | Modelo e medições |
| R03 Receita não faturada | Ocorrência, corte | Saldo e PAA | I | Controles de medição |
| R06 Dívidas | Integridade, classificação | Notas 18–19; vencimentos | P | Confirmações CF-04 |
| R07 Provisões | Integridade, avaliação | Movimentação e casos | P | Carta jurídica CF-08 |
| R13 Partes relacionadas | Integridade | Nota 31 conciliada | P | Atas e confirmações |
| R16 Burla de controles | Todas | Indicador no VNR | I | Teste de lançamentos |
| R17 Continuidade | Divulgação | Liquidez e release | P | Previsão de caixa |
| Saldos de abertura | Todas | 61 linhas sem diferença | S | Papéis do antecessor |
| Eventos subsequentes | Integridade | Notas, ITRs, RI até 23/10/2026 | P | Indagações e carta |

**Inconsistências entre fontes (item 11).** DV01–DV20 (Apêndice A) foram resolvidas a favor da fonte primária com página. Nenhuma ficou sem tratamento. O FR truncado (DV15) e o relatório de 2024 ausente (DV20) são limitações, não inconsistências.

**Conclusão de suficiência.** Para três riscos significativos (R02, R03, R16) a evidência é insuficiente, e os procedimentos continuam planejados. Para o R01, a evidência é parcial e a base sintética só demonstra método. Isso impediria opinião numa auditoria real; aqui sustenta somente as conclusões limitadas do dossiê.
"""
UPDATES = {
 "PT 450": dict(situacao="Concluído (B08/B11)",
   titulo="Avaliação das distorções identificadas — consolidação final (sintética, pública e hipóteses)",
   proc_fix={"450-05": "Realizado com evidência pública (consolidação) / Simulado para fins didáticos (parcela sintética)"},
   corpo_add=ADD_450,
   resultados="Nenhuma distorção real da CPFL sustentada por evidência pública. Distorção sintética líquida de R$ 117,5 milhões (38,7% da execução), acumulada só na simulação. Duas hipóteses (IRRF Jantus e VNR) não acumuladas, somando 69% da global no pior caso. Divergências do preparador excluídas.",
   conclusao="Não foram identificadas distorções reais a acumular. As distorções sintéticas não são relevantes frente à global e seriam comunicadas com pedido de correção. As hipóteses DH-01 e DH-02 são o risco remanescente e dependem de acesso. Não é conclusão sobre a CPFL.",
   evidencias_add=f" Bloco 11: {PLAN} (PT450_Consolidado)."),
 "PT 500": dict(situacao="Concluído (B07/B11)",
   titulo="Evidência de auditoria — base sintética, conciliação e matriz de suficiência por afirmação",
   corpo_add=ADD_500,
   resultados="Base sintética íntegra e conciliada (B07). Matriz de evidência: 1 área suficiente, 7 parciais e 3 riscos significativos (R02, R03, R16) com evidência insuficiente. Inconsistências DV01–DV20 tratadas.",
   conclusao="A evidência pública é relevante e confiável (DF auditadas), mas insuficiente para segurança razoável nos riscos significativos. Sustenta só as conclusões limitadas e não profissionais deste dossiê. Não é conclusão sobre a CPFL.",
   evidencias_add=f" Bloco 11: {PLAN} (PT500_Matriz)."),
}

CONCLUSAO_MD = """# 7. Conclusão integrada do trabalho (sem opinião profissional)

> Esta seção **não é opinião de auditoria** e não fornece asseguração. Resume o que foi feito, o que a evidência pública sustenta e o que fica pendente.

**7.1 O que foi feito**

- 27 PTs nas NBC TA aplicáveis a 2025, com os 9 campos mínimos (mais o campo de requisito × orientação × julgamento), 6 programas por ciclo e o programa de consolidação (PG-CONS).
- Toda informação cita documento e página. Cada procedimento tem modalidade: realizado com evidência pública, planejado por falta de acesso ou simulado.
- Base sintética de 501.000 registros do ativo financeiro da concessão, conciliada ao saldo publicado (R$ 29.623.619 mil), com testes pré-registrados e congelados antes da consulta ao gabarito.

**7.2 O que a evidência pública sustenta**

| Área | Resultado |
|---|---|
| Consistência interna das DF | Demonstrações, notas, segmentos e saldos de abertura conciliados, sem diferença além de arredondamento |
| Ativo financeiro da concessão | Movimentação e saldos por distribuidora conciliados. VNR de 2025 acima da expectativa (+12,2%; Paulista) sem explicação pública |
| Litígios | Provisões e perdas possíveis conciliadas. IRRF Jantus: obrigação em 31/12/2025, reconhecimento a verificar |
| Partes relacionadas | Saldos da nota 31 conciliados com o balanço. Completude não verificável |
| Eventos subsequentes | Renovação das concessões (2026) tratada como evento novo, sem ajuste nas DF de 2025 |
| Continuidade | CCL negativo, mas sem condição que, com a evidência pública, indique dúvida significativa |
| Distorções | Nenhuma distorção real sustentada. Hipóteses não acumuladas |
| Controles | Nenhuma deficiência significativa identificada; nenhum controle testado |

**7.3 O que a simulação demonstra (não é sobre a CPFL)**

- Testes integrais detectaram 100% das distorções de valor e existência inseridas e 99,6% das de categoria, sem falso positivo.
- MUS ampliado: distorção conhecida + UML residual = R$ 303,2 milhões, dentro da tolerável. Margem estreita.
- **Não é teste cego independente**: a mesma IA desenhou os erros e os testes.

**7.4 O que impediria uma opinião numa auditoria real**

1. Evidência insuficiente nos riscos significativos R02, R03 e R16, e parcial no R01 (PT 500).
2. Nenhum teste de controles, confirmação externa, indagação, inspeção física ou carta de representação. Todos estão desenhados e **não executados**.
3. Duas hipóteses sem resposta: o VNR da Paulista e o reconhecimento do IRRF Jantus.

**7.5 Próximos passos que uma equipe com acesso faria primeiro**

1. Obter o cálculo do VNR por distribuidora e a base de remuneração homologada.
2. Confirmar o lançamento do IRRF Jantus.
3. Testar lançamentos manuais (NBC TA 240) e controles de medição e faturamento.
4. Enviar as confirmações CF-01 a CF-08 e obter a carta de representação.
"""

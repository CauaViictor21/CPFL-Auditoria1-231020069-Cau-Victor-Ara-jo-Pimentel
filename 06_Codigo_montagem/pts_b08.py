# -*- coding: utf-8 -*-
"""PTs do Bloco 08: PT 530 (concluído) e PT 450 (parcela simulada; fechamento no Bloco 11)."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "23/10/2026"
PLAN = "CPFL_B08_Amostragem_Testes_Distorcoes.xlsx"
PTS = []

PTS.append(dict(
codigo="PT 530", titulo="Amostragem em auditoria — ativo financeiro da concessão (base sintética)",
norma="NBC TA 530 (Res. CFC 1.222/2009; NORMAS p. 530–548). Itens: 5 (definições: amostragem, risco de amostragem, anomalia, amostragem estatística, distorção tolerável; p. 533–534), 6–8 (definição, tamanho e seleção; p. 535), 9–11 (execução e substituição), 12–13 (natureza e causa; anomalia), 14 (projeção; p. 536), 15 (avaliação); A3 (distorção tolerável), A10–A13 (tamanho e seleção; p. 538), A18–A23 (projeção e avaliação; p. 539–540); Apêndice 3 (fatores de tamanho em testes de detalhes; p. 544–545) e Apêndice 4 (métodos de seleção; p. 547). Apoio: NBC TA 500 item 10 (p. 449) e NBC TA 330 item 21 (p. 384).",
objetivo="Obter base razoável para concluir se o saldo registrado do ativo financeiro da concessão (base sintética de 501.000 registros) contém superavaliação acima da distorção tolerável. Combina procedimentos integrais por computador e amostragem estatística por unidade monetária.",
conta="Ativo financeiro da concessão: R$ 29.623.619 mil (DF25 BP p. 34; nota 11 p. 68). Base SINTÉTICA v2 conciliada no PT 500.",
afirmacoes="Existência e direitos (duplicidades, bens baixados), avaliação (valor do bem) e classificação (categoria). Risco significativo R01 (PT 315), resposta exclusivamente substantiva (PT 330).",
populacao=f"501.000 registros; R$ 29.623.619.000,00; SHA-256 877d4a02…4bb0 (conferido pelo código). Completude: conciliação do Bloco 07. Unidade amostral do MUS: cada real do saldo. Amostra: saida_b08/MUS_amostra_resultados.csv (385 itens) e MUS_ampliacao_residual.csv (492 itens). Memória de cálculo: {PLAN}.",
procedimentos=[
 ("530-01", "Registrar o desenho (objetivo, população, unidade, método, parâmetros, regras de decisão) no Drive antes da execução — 23/10/2026 19:54", "Realizado com evidência pública (registro documental)"),
 ("530-02", "T1–T4: testes integrais por computador em 100% da população (não são amostragem)", "Simulado para fins didáticos"),
 ("530-03", "MUS: dimensionar (n = 385), selecionar sistematicamente com semente e avaliar pelo limite de Stringer a 95%", "Simulado para fins didáticos"),
 ("530-04", "Investigar natureza e causa das distorções da amostra; ampliar a amostra na população residual (n2 = 492)", "Simulado para fins didáticos"),
 ("530-05", "Congelar código, parâmetros, seleção, resultados e hashes no Drive (19:55:53) antes de abrir o registro reservado de erros", "Realizado com evidência pública (registro documental)"),
 ("530-06", "Comparar com o registro reservado: detecções, omissões, falsos positivos e cobertura do limite", "Simulado para fins didáticos"),
 ("530-07", "Na CPFL real: inspecionar laudo de VNR, base de remuneração homologada e existência física dos itens sorteados", "Planejado por falta de acesso"),
],
corpo="""
**1. Escolha do desenho e o que é julgamento**

| Elemento | Escolha | Exigência normativa ou julgamento |
|---|---|---|
| Tipo de teste | Testes de detalhes. Não há testes de controles (não testados) | Item 1; 330 item 21: risco significativo só com substantivos exige testes de detalhes |
| Procedimentos integrais | T1 duplicidade, T2 baixado com valor, T3 recálculo (limite de 1%), T4 coerência residual × categoria (limite de 0,00015) | Julgamento. Não é amostragem (item 5) |
| Amostragem | **Estatística**: seleção aleatória (ponto inicial com semente) **e** avaliação por teoria das probabilidades (Poisson) | Atributos (a) e (b) do item 5 |
| Método | Unidade monetária (MUS), sistemático por intervalo | Apêndice 4. Adequado a superavaliação de saldos de ativo |
| Distorção tolerável | R$ 303.421.730 = materialidade de execução | A3: pode ser igual ou menor. Julgamento (D-B04-01) |
| Risco de aceitação incorreta | 5% | Julgamento: risco significativo, sem confiança em controles (Apêndice 3) |
| Distorção esperada | R$ 45.513.259,50 (15% da DT) | Julgamento didático fixado antes dos testes |
| Fator de expansão | 1,6 | Literatura (AICPA, *Audit Sampling*), não norma |

O tamanho não decorre de regra arbitrária, como "30 itens". Decorre da fórmula n = VC × FC ÷ (DT − DE × FE) = 29.623.619.000 × 2,9957 ÷ (303.421.730 − 1,6 × 45.513.259,50) = **385**. O intervalo é J = R$ 76.944.464,94 e o ponto inicial, R$ 26.922.277,72.

- **Saldos nulos ou negativos:** não há; o código para se houver.
- **Itens ≥ J:** nenhum (o maior tem cerca de R$ 3,6 milhões). Por isso não há estrato de seleção integral.
- **Seleção repetida:** nenhum item foi selecionado mais de uma vez.
- **Estratificação:** feita implicitamente pelo valor. As subestações, com 3% das linhas e 52% do valor, recebem mais pontos de seleção.

**2. Resultados dos testes integrais (100%)**

| Teste | Itens | Efeito no saldo (R$) |
|---|---:|---:|
| T1 duplicidades (registros excedentes; 1.000 pares com atributos idênticos) | 1.000 | 59.975.200,49 |
| T2 bens BAIXADOS com valor | 1.000 | 56.070.250,89 |
| T3 superavaliação (> 1%) | 1.000 | 8.250.695,88 |
| T3 subavaliação (< −1%) | 1.000 | (6.811.809,08) |
| T4 residual incoerente com a categoria cadastrada | 996 | — (classificação) |
| **Distorção conhecida líquida** | | **117.484.338,18** |

**3. Resultado da amostra MUS e resposta**

- **Amostra.** Dos 385 itens, 6 tinham distorção: 4 superavaliações (2 BAIXADO e 2 registros excedentes de duplicidade, *taint* 100%) e 2 subavaliações.
  - Distorção projetada de superavaliação: R$ 307.777.859,74.
  - Precisão básica: R$ 230.505.016,88.
  - Limite superior (UML): **R$ 704.312.623,78 > DT** (aba Avaliacao_MUS).
- **Leitura correta dos três números:**
  - a **soma das distorções da amostra** é R$ 1.534.709,56;
  - a **distorção projetada** estende essas distorções à população;
  - o **limite superior** soma a projeção ao risco de amostragem.

  Nenhum deles é a distorção real da população.
- **Natureza e causa (item 12).** Todas as 6 distorções pertencem a classes que os testes integrais identificaram por completo. São sistemáticas e **não são anomalias**, então o item 13 não se aplica. A distorção dessas classes é **conhecida**, não projetada.
- **Ampliação antes de afirmar suficiência (item 15(b)).**
  - A população residual exclui os 4.000 registros sinalizados: R$ 29.379.887.051,80.
  - A folga é a DT menos a superavaliação conhecida bruta (R$ 124.296.147,26): R$ 179.125.582,74.
  - Nova amostra independente (semente 2310200699): n2 = 492, J2 = R$ 59.715.217,58. Resultado: **0 distorções**; 2 itens com incoerência de categoria, sem efeito monetário.
  - UML residual = 2,9957 × J2 = R$ 178.890.804,54.
  - **Superavaliação conhecida + UML residual = R$ 303.186.951,80 ≤ DT (R$ 303.421.730).**

**4. Comparação com o registro reservado (feita após o congelamento)**

| Teste × tipo de erro | Verdadeiros | Detectados | Omitidos | Falsos positivos |
|---|---:|---:|---:|---:|
| T1 duplicidade (nível de par) | 1.000 | 1.000 | 0 | 0 |
| T2 baixado mantido | 1.000 | 1.000 | 0 | 0 |
| T3 superavaliação | 1.000 | 1.000 | 0 | 0 |
| T3 subavaliação | 1.000 | 1.000 | 0 | 0 |
| T4 classificação incorreta | 1.000 | 996 | 4 | 0 |

- **Efeito monetário.** O efeito estimado é igual ao verdadeiro em todos os tipos (diferença total de R$ 0,02, de arredondamento). A ponte confere: publicado R$ 29.623.619.000,00 − efeito R$ 117.484.338,16 = referência R$ 29.506.134.661,84.
- **Omissões do T4.** As 4 omissões são bens totalmente depreciados (residual no piso de 0,01). Nesse nível, o residual não distingue a categoria. É uma limitação do teste, que **não** foi ajustado depois de conhecido o resultado.
- **Convenção do T1.** A regra "id maior = excedente" acertou o registro em 497 de 1.000 casos. O par e o valor estão sempre certos, mas a identificação de qual é o original exigiria documento (data de cadastro).
- **Projeção da amostra original.** A projeção (R$ 307,8 milhões) superou a verdade (R$ 124,3 milhões) em R$ 183,5 milhões. O erro de projeção é esperado com poucos erros de *taint* 100%. O UML cobriu a verdade, como deve ocorrer em pelo menos 95% das amostras.

**5. O que isto demonstra e o que não demonstra**

- **Demonstra:** a execução reproduzível do desenho, da seleção, da projeção, da avaliação e da ampliação.
- **Não demonstra:** eficácia em dados reais. A mesma IA desenhou os erros e os testes, e o "valor auditado" de cada item sorteado foi obtido pelas mesmas regras T1–T3. A amostra não poderia revelar tipos de erro fora dessas regras.

Na CPFL real, os itens sorteados seriam testados contra documentos e inspeção física (530-07, planejado).
""",
evidencias=f"B08_Desenho_pre_registro.md e B08_congelamento.json (Drive 04_Testes; registrados às 19:54 e 19:55:53 de 23/10/2026); testes_b08.py, avaliacao_complementar_b08.py, comparar_gabarito_b08.py, parametros_b08.json; saídas em saida_b08/; {PLAN}. Referências cruzadas: PT 315 (R01), PT 320, PT 330, PT 450, PT 500.",
resultados="Testes integrais: 4.000 registros com distorção de valor ou existência e 996 com incoerência de categoria. Distorção conhecida líquida de R$ 117,5 milhões. MUS inicial: UML de R$ 704,3 milhões > DT, o que levou à ampliação. Ampliação: 0 distorções em 492 itens. Conhecida + UML residual = R$ 303,19 milhões ≤ DT. Pós-congelamento: 100% de detecção em T1–T3, 99,6% em T4, 0 falsos positivos.",
conclusao="No ambiente simulado, a combinação de testes integrais e MUS ampliado forneceu base razoável (item 15) para concluir que a superavaliação não corrigida não excede a distorção tolerável, desde que a distorção conhecida seja tratada no PT 450. A margem é estreita (99,9% da DT), o que reforça a solicitação de correção. Não é conclusão sobre a CPFL.",
limitacoes="Base 100% sintética. Os parâmetros DT, risco, DE e FE são julgamentos didáticos. Não é teste cego independente. O MUS é fraco para subavaliação (coberta pelo T3). A identificação do registro excedente no T1 é convencional. O T4 não distingue categorias no piso de depreciação.",
))

PTS.append(dict(
codigo="PT 450", situacao="Parcela simulada redigida (fechamento no B11)",
titulo="Avaliação das distorções identificadas — parcela simulada (base sintética)",
norma="NBC TA 450 (R1) (DOU 05/09/2016; NORMAS p. 427–445). Itens: 4 (definição de distorção), 5 (acumulação; p. 429), 6 (revisão da estratégia quando as distorções se aproximam da materialidade), 8 (comunicação e correção; p. 430), 10 (revisão da materialidade), 11 (relevância individual e em conjunto); A2–A6 (claramente trivial; distorção factual, de julgamento e projetada; p. 433–434).",
objetivo="Acumular e avaliar as distorções identificadas na base sintética do ativo financeiro da concessão, frente à materialidade aprovada (D-B04-01), e definir o tratamento: comunicação, correção e efeito na estratégia.",
conta="Ativo financeiro da concessão (simulado) e contrapartida no resultado (ajuste a valor justo e baixas, nota 11 p. 68; receita, nota 26).",
afirmacoes="Existência, avaliação e classificação (R01).",
populacao=f"Resultados do PT 530: T1–T4 e MUS ampliado; {PLAN}, aba PT450_Distorcoes.",
procedimentos=[
 ("450-01", "Acumular as distorções que não sejam claramente triviais, avaliando individualmente e em conjunto (A2)", "Simulado para fins didáticos"),
 ("450-02", "Classificar como factual, de julgamento ou projetada (A6)", "Simulado para fins didáticos"),
 ("450-03", "Comparar com a materialidade e verificar o gatilho de D-B04-01 (item 6)", "Simulado para fins didáticos"),
 ("450-04", "Comunicar à administração e solicitar correção (item 8)", "Planejado por falta de acesso (nenhuma comunicação enviada)"),
 ("450-05", "Consolidar com as distorções dos demais PTs e avaliar o efeito nas DF (itens 10–11)", "Realizado com evidência pública (consolidação) / Simulado para fins didáticos (parcela sintética)"),
],
corpo="""
**1. Acumulação (item 5 e A2)**

Cada distorção individual é menor que o limite de trivialidade (R$ 20.228.120), porque o maior item da base tem cerca de R$ 3,6 milhões. Em conjunto, porém, as classes não são triviais, e A2 exige julgamento "individualmente ou em conjunto". Por isso as classes são acumuladas:

| Classe | Valor (R$) | % da execução | % da global | Tipo (A6) |
|---|---:|---:|---:|---|
| Duplicidades (T1) | 59.975.200,49 | 19,8% | 14,8% | Factual (na simulação) |
| Bens baixados mantidos (T2) | 56.070.250,89 | 18,5% | 13,9% | Factual |
| Superavaliação de valor (T3+) | 8.250.695,88 | 2,7% | 2,0% | Factual |
| Subavaliação de valor (T3−) | (6.811.809,08) | (2,2%) | (1,7%) | Factual |
| Classificação de categoria (T4) | — | — | — | Por natureza (A5) |
| **Distorção líquida acumulada** | **117.484.338,18** | **38,7%** | **29,0%** | Superavaliação |

- Não há distorção **projetada** a acumular: as classes foram identificadas em 100% da população. A margem do UML residual (R$ 178,9 milhões) é **risco de amostragem**, não distorção.
- Não há distorção **de julgamento** na parcela simulada. A avaliação das premissas de VNR fica no PT 540.

**2. Efeito na estratégia (item 6) e na materialidade**

- A superavaliação bruta (R$ 124,3 milhões) é 41,0% da materialidade de execução, abaixo do gatilho de 50% de D-B04-01. A materialidade de execução fica mantida em 75%.
- Somando a margem de amostragem, chega-se a R$ 303,2 milhões, ou 99,9% da execução e 74,9% da global. Isso caracteriza aproximação da materialidade (item 6(b)). Resposta: solicitar a correção da distorção conhecida e reavaliar no Bloco 11 com as distorções dos demais PTs.
- Se a contrapartida for o resultado, o efeito no LAIR é de 1,45% (LAIR de R$ 8.091.246 mil, DF25 DRE p. 36/4).

**3. Comunicação e correção (item 8)**

Na auditoria real, as distorções seriam comunicadas tempestivamente à administração, com pedido de correção. Isso abrangeria a baixa dos registros duplicados e dos bens baixados e o ajuste dos valores recalculados. **Nenhuma comunicação foi enviada à CPFL** (Planejado por falta de acesso). Se a administração recusasse a correção, as razões seriam obtidas e avaliadas (item 9).

**4. Classificação (A5)**

A categoria do bem não é divulgada nas DF, então a classificação incorreta não altera o saldo nem a divulgação. Ela indica uma fragilidade de cadastro, que seria comunicada como possível deficiência de controle (PT 265, Bloco 11).
""",
evidencias=f"{PLAN} (Testes_100, Ampliacao, PT450_Distorcoes); PT 530; DF25 p. 36 e 68; D-B04-01. Referências cruzadas: PT 260, PT 265, PT 320, PT 540, PT 580.",
resultados="Distorção líquida acumulada de R$ 117,5 milhões de superavaliação (38,7% da execução; 29,0% da global). Gatilho de D-B04-01 não acionado. Aproximação da materialidade quando se considera a margem de amostragem.",
conclusao="Na simulação, a distorção acumulada não é relevante individualmente nem em conjunto frente à materialidade global, mas deve ser comunicada e sua correção solicitada. Avaliação final no Bloco 11, com as demais distorções. Não é conclusão sobre a CPFL.",
limitacoes="Distorções da base sintética, sem relação com a CPFL real. Nenhuma comunicação foi enviada. A contrapartida contábil é presumida (resultado), para fins de ordem de grandeza.",
))

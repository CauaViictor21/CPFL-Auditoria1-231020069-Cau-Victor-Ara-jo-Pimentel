# -*- coding: utf-8 -*-
"""PTs do Bloco 07: PT 500 (iniciado; fechamento no Bloco 11)."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "23/10/2026"
PLAN = "CPFL_B07_Conciliacao_Verificacoes_Base.xlsx"
PTS = []

PTS.append(dict(
codigo="PT 500", situacao="Iniciado (fechamento no B11)", titulo="Evidência de auditoria — base sintética do ativo financeiro da concessão e sua conciliação (em andamento)",
norma="NBC TA 500 (R1) (DOU 05/09/2016; NORMAS p. 446–450). Itens: 5 (definições: registros contábeis, adequação, suficiência), 6 (procedimentos apropriados), 7 (relevância e confiabilidade), 9 (informações produzidas pela entidade: exatidão, integridade, precisão e detalhamento; p. 449), 10 (seleção de itens), 11 (inconsistências). Apoio: NBC TA 530 e 450 (Bloco 08) e NBC TA 540 (R2) (Bloco 09).",
objetivo="Avaliar se a população que sustenta o ativo financeiro da concessão (R$ 29.623.619 mil) é exata, íntegra e detalhada o bastante para os testes do Bloco 08. Documentar a base sintética que substitui o cadastro real inacessível e registrar o que a simulação pode e não pode demonstrar.",
conta="Ativo financeiro da concessão (consolidado, não circulante): R$ 29.623.619 mil, 36,5% do ativo total (DF25 BP p. 34; nota 11 p. 68). Composição por distribuidora nas DFs individuais (Paulista, RGE, Piratininga) e por diferença (Santa Cruz).",
afirmacoes="Existência, direitos, avaliação e classificação (risco significativo R01 do PT 315; PAA 3 da PwC, DF25 p. 29). Neste bloco: integridade e exatidão da informação produzida pela entidade (item 9), como pré-condição dos testes.",
populacao=f"Base SINTÉTICA v2: 501.000 registros (500.000 bens de referência + 1.000 linhas adicionais previstas no desenho), arquivo CPFL_SINTETICA_Base_AFC_2025_registrada.csv.gz, SHA-256 877d4a02…4bb0. Projeto: CPFL_B06_Projeto_Base_Sintetica.pdf. Conciliação: {PLAN}.",
procedimentos=[
 ("500-01", "Reexecutar a movimentação da nota 11 e conciliar com BP, DRE e DFC (B02, CC05/CC06)", "Realizado com evidência pública"),
 ("500-02", "Conciliar os saldos das quatro distribuidoras com o consolidado (3 DFs individuais + Santa Cruz por diferença, provada pela movimentação)", "Realizado com evidência pública"),
 ("500-03", "Gerar a base sintética com semente fixa e reproduzi-la em pasta limpa (mesmo hash)", "Simulado para fins didáticos"),
 ("500-04", "Conciliar a base com o saldo publicado, no total e por distribuidora (diferença R$ 0,00)", "Simulado para fins didáticos"),
 ("500-05", "Testar a integridade da listagem: contagem, chaves, domínios, datas, precisão, vazios, coerência agregada", "Simulado para fins didáticos"),
 ("500-06", "Obter o cadastro real de bens e a base de remuneração homologada pela ANEEL e conciliar com o razão e o laudo de VNR", "Planejado por falta de acesso"),
 ("500-07", "Avaliar o especialista da administração (laudo de avaliação) — itens 8 e A34–A48", "Planejado por falta de acesso"),
],
corpo="""
**1. Por que uma base sintética e o que ela substitui**

- **Na auditoria real**, o auditor receberia da CPFL a listagem dos bens que compõem a base de remuneração e o cálculo do direito de indenização (DF25 nota 4, p. 59). Essa listagem é **informação produzida pela entidade**. Antes de usá-la, o auditor precisa testar se ela é **exata e íntegra** (item 9(a)) e **precisa e detalhada** o bastante (item 9(b)).
- **Neste trabalho** não há acesso ao cadastro. A base sintética faz o papel dessa listagem para que os procedimentos de conciliação, amostragem e avaliação de distorções possam ser executados (Simulado para fins didáticos).

**2. Evidência real que ancora a simulação**

| Fato | Valor (R$ mil) | Fonte | Modalidade |
|---|---:|---|---|
| Saldo consolidado | 29.623.619 | DF25 BP p. 34; nota 11 p. 68 | Realizado com evidência pública |
| CPFL Paulista | 12.617.237 | DF Paulista, nota 11, p. 29 (impressa) | Realizado com evidência pública |
| RGE | 12.734.234 | DF RGE, nota 11, p. 31 (impressa) | Realizado com evidência pública |
| CPFL Piratininga | 3.836.600 | DF Piratininga, nota 11, p. 29 (impressa) | Realizado com evidência pública |
| CPFL Santa Cruz | 435.548 | Por diferença; reconstruída pela movimentação: 435.547 (±1, arredondamento) | Realizado com evidência pública (cálculo) |

A movimentação de 2025 da Santa Cruz foi obtida como consolidado menos as três DFs individuais:

- saldo de 2024: 249.934;
- VNR: 9.193;
- transferências do ativo contratual: 178.783;
- transferências para o intangível: (989);
- baixas: (1.374).

O resultado confirma que não há eliminações de consolidação relevantes nesta conta.

**3. Conciliação e integridade da base (leitura do arquivo salvo)**

| Verificação | Resultado | Critério |
|---|---|---|
| Linhas de dados / IDs únicos | 501.000 / 501.000 | Igual ao desenho |
| Falhas de formato, domínio, data, precisão, intervalo (16 testes) | 0 | 0 |
| Total da base − saldo do BP | R$ 0,00 | R$ 0,00 |
| Diferença por distribuidora (4) | R$ 0,00 em todas | R$ 0,00 |
| Mediana de valor ÷ (VNR × fator × residual) | Igual ao fator de escala divulgado (desvio < 0,000001) | Coerência agregada |
| Reprodução em pasta limpa | 4 arquivos com hash idêntico | Igual |
| `id_bem_tecnico` repetidos | 1.000 pares | **Exceção prevista no desenho**: será investigada no PT 530 |
| Registros BAIXADO com valor | 1.000 | **Exceção prevista no desenho**: será investigada no PT 530 |

As duas últimas linhas **não são falhas de geração**. São exceções que o desenho insere de propósito e que os testes do Bloco 08 precisam tratar como achados.

Super e subavaliação e classificação incorreta não aparecem nas verificações estruturais. Elas dependem do recálculo e dos testes analíticos do Bloco 08.

**4. Relevância e confiabilidade (itens 7 e 9)**

- **O que está demonstrado.** A conciliação prova apenas que a **listagem soma o razão**. Ela **não** prova existência, titularidade nem mensuração. O fechamento com o saldo publicado é uma restrição matemática da simulação, imposta por um fator de escala único e divulgado por distribuidora (1,27 a 1,34).
- **O que seria exigido na auditoria real:**
  - conciliar a listagem com o razão e com a base de remuneração homologada pela ANEEL;
  - testar os controles de cadastro de bens (unitização e baixas);
  - avaliar o especialista que calcula o VNR;
  - inspecionar fisicamente uma amostra de bens.
- **Confiabilidade das fontes:** DF auditadas pela PwC, com relatório sem modificação (DF25 p. 26–32), formam a evidência externa e documental de maior confiabilidade disponível. A base sintética não tem valor probatório sobre a CPFL.

**5. Controle de independência entre geração e teste**

- **Pasta reservada.** O registro de erros, a base de referência e a ponte de efeitos estão em pasta reservada. Eles **não foram lidos** neste bloco e têm os hashes registrados:
  - registro de erros 45e3ec3e…;
  - referência 48652ae2…;
  - ponte 7eabcc92….
- **Limite da independência.** A mesma IA desenhou os erros e fará os testes. Por isso, os resultados do Bloco 08 **não** serão apresentados como teste cego independente.

**6. Atualização em 23/10/2026 (Bloco 08): uso da base como evidência simulada**

- A base congelada no Bloco 07 (mesmo SHA-256) foi a única fonte dos testes do PT 530. O código conferiu o hash antes de ler os dados.
- Os testes integrais identificaram 4.000 registros com distorção de valor ou de existência (T1, T2 e T3) e 996 com incoerência de categoria (T4).
- A distorção conhecida líquida é de R$ 117.484.338,18, uma superavaliação do saldo registrado (PT 450).
- Relevância (item 7): os testes avaliam existência, avaliação e classificação com regras ligadas aos atributos de cada registro.
- Confiabilidade: na simulação, ela depende da coerência interna da base, e não de fonte externa. Por isso o resultado vale como demonstração de método, não como evidência sobre a CPFL.

**7. Pendente para o fechamento deste PT (Bloco 11)**

- consolidar a suficiência e a adequação da evidência por afirmação, a partir dos resultados dos PTs 505, 520, 530, 540 e 550;
- registrar as inconsistências entre fontes (item 11), como DV01–DV18 do Apêndice A.
""",
evidencias=f"DF25 p. 26–32, 34, 59, 68; DFs individuais (pasta 06); {PLAN} (Conciliacao, Verificacoes, Execucao); CPFL_B06_Projeto_Base_Sintetica.pdf; gerar_base_cpfl_v2.py, verificar_base_cpfl_v2.py, config_base_cpfl_v2.json. Referências cruzadas: PT 315 (R01), PT 320, PT 530, PT 450, PT 540.",
resultados="Base de 501.000 registros conciliada com R$ 29.623.619 mil, no total e nas quatro distribuidoras, sem diferença. Nenhuma falha de geração. Reprodução em pasta limpa com hashes idênticos. Duas classes de exceção previstas no desenho foram registradas para investigação no PT 530.",
conclusao="A listagem sintética é íntegra e exata em relação ao saldo publicado e está apta a ser usada nos testes do Bloco 08. Isso vale apenas no ambiente simulado. A evidência sobre a conta real limita-se às DFs auditadas, consolidada e individuais. PT em andamento: fechamento no Bloco 11.",
limitacoes="Base 100% sintética. Pesos, valores unitários, vidas úteis, datas e fatores são premissas arbitradas. Só os saldos e a natureza da conta são reais. O saldo da Santa Cruz foi derivado por diferença (sem DF própria no Drive). Não houve acesso ao cadastro, à base de remuneração da ANEEL nem ao laudo de VNR.",
))

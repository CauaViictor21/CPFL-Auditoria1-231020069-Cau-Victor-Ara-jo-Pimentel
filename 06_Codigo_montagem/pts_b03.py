# -*- coding: utf-8 -*-
"""Conteúdo dos papéis de trabalho do Bloco 03 (PT EC, 200, 210, 220, 230).
Cada PT segue o modelo único (9 campos do enunciado + modalidade por procedimento).
Fontes: DF25 = DF25 CPFL.pdf (pág. física/impressa); NORMAS = CONSOLIDAÇÃO DAS NORMAS AUD 1.pdf (pág. do PDF);
ITR3T25 = ITR 3TRI 2025.pdf (pág. do PDF)."""

PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "22/10/2026"

PTS = []

# --------------------------------------------------------------------------- EC
PTS.append(dict(
codigo="PT EC", titulo="Estrutura Conceitual — caracterização do trabalho de asseguração",
norma="NBC TA Estrutura Conceitual para Trabalhos de Asseguração (DOU 25/11/2015; efeitos a partir de 01/01/2016 — NORMAS p. 24). Itens: 2, 10, 12–16, 26–27, 35, 39–49 (objeto e critérios), 50–82 (evidências), 83–92 (relatório).",
objetivo="Caracterizar o trabalho de auditoria das demonstrações contábeis consolidadas de 2025 da CPFL Energia S.A. como trabalho de asseguração razoável: partes, objeto, critérios, evidência e relatório. Diferenciá-lo de outros trabalhos de asseguração e de serviços correlatos. Deixar explícito o que este dossiê acadêmico **não** fornece.",
conta="Demonstrações contábeis individuais e consolidadas de 31/12/2025 (BP, DRE, DRA, DMPL, DFC, DVA e notas) — DF25 p. 33–115.",
afirmacoes="Não se aplicam afirmações por conta neste PT, que trata do enquadramento do trabalho. Risco tratado: **risco de caracterização indevida**, ou seja, apresentar este exercício acadêmico como se fornecesse asseguração. Resposta: avisos em todos os PTs e na conclusão.",
populacao="Fontes: (1) NORMAS, Estrutura Conceitual, p. 3–28; (2) DF25 p. 26–32 (relatório do auditor 2025) e p. 45 (nota 2.1); (3) ITR3T25 p. 14–15 (relatório de revisão do 3T25). Seleção: todas as fontes que caracterizam o trabalho real e um exemplo real de trabalho diferente (revisão de ITR).",
procedimentos=[
 ("EC-01","Identificar as três partes do trabalho (EC item 27) para a auditoria de 2025","Realizado com evidência pública"),
 ("EC-02","Identificar objeto e critérios aplicáveis (EC itens 39–49) a partir da nota 2 da DF25","Realizado com evidência pública"),
 ("EC-03","Classificar o nível de asseguração (EC itens 14–15) do relatório de 2025 e de um relatório de revisão real (ITR 3T25)","Realizado com evidência pública"),
 ("EC-04","Montar quadro comparativo: auditoria × revisão × outros trabalhos de asseguração × serviços correlatos","Realizado com evidência pública (exemplos não CPFL rotulados como genéricos)"),
 ("EC-05","Definir o que este dossiê entrega e o que não entrega (nível de asseguração = nenhum)","Realizado com evidência pública"),
],
corpo="""
**1. Elementos do trabalho real (auditoria 2025)**

| Elemento (EC item 26) | Auditoria das DF 2025 da CPFL Energia | Fonte |
|---|---|---|
| Auditor independente | PricewaterhouseCoopers Auditores Independentes Ltda. (CRC 2SP027613/F-1) | DF25 p. 26 e 32 |
| Parte responsável | Administração da CPFL Energia (DF autorizadas em 23/02/2026) e Conselho de Administração (aprovação em 04/03/2026) | DF25 p. 45/13 |
| Usuários previstos (EC item 35) | Acionistas — o controlador State Grid Brazil Power e os minoritários do Novo Mercado (CPFE3) —, credores de debêntures e empréstimos, CVM e mercado. A ANEEL usa as demonstrações regulatórias, que são outro objeto | Relatório endereçado "Aos Administradores e Acionistas" (DF25 p. 26); FR 2025 v6 item 1.1 |
| Objeto (itens 39–41) | Posição patrimonial e financeira em 31/12/2025, desempenho e fluxos de caixa de 2025 (individual e consolidado) | DF25 p. 26 |
| Critérios (itens 42–49) | Práticas contábeis adotadas no Brasil (CPC/CVM) e IFRS do IASB; orientações do MCSE/ANEEL quando aplicáveis | DF25 p. 45/13 (nota 2.1) |
| Evidência (itens 50–82) | Apropriada e suficiente, obtida pela firma (procedimentos descritos nos PAA) | DF25 p. 27–29 |
| Relatório (itens 83–92) | Opinião sem modificação, em forma positiva | DF25 p. 26 |

**2. Nível de asseguração: comparação com casos reais da própria CPFL**

| Aspecto | Auditoria anual 2025 | Revisão do ITR 3T25 |
|---|---|---|
| Norma | NBC TA (relatório cita normas brasileiras e internacionais de auditoria) | NBC TR 2410 / ISRE 2410 (ITR3T25 p. 14) |
| Nível (EC 14–15) | Asseguração **razoável**: risco reduzido a nível aceitavelmente baixo | Asseguração **limitada**: risco maior que na auditoria |
| Procedimentos | Avaliação de riscos, testes de controles e substantivos (DF25 p. 27–29) | Principalmente indagações e procedimentos analíticos (ITR3T25 p. 14) |
| Forma da conclusão | Positiva ("apresentam adequadamente…", DF25 p. 26) | Negativa ("não temos conhecimento de nenhum fato…", ITR3T25 p. 15) |
| Data | 04/03/2026 | 05/11/2025 |

**3. Outros trabalhos (para diferenciação)**

- *Outros trabalhos de asseguração* (EC itens 12–13). São trabalhos de atestação ou diretos sobre objetos diferentes de DF históricas, como informações de sustentabilidade ou controles. Os exemplos são genéricos: não foi verificado se a CPFL contratou trabalhos desse tipo.
- *Serviços correlatos sem asseguração*. Exemplos: procedimentos previamente acordados e carta-conforto em oferta de valores mobiliários (CTA 23, listado pelo CFC). Não expressam conclusão de asseguração. O EC item 25 veda trocar um trabalho de asseguração por outro sem asseguração sem justificativa razoável.
- A Estrutura Conceitual **não é norma** e não cria requisitos (EC item 2). Ela orienta a leitura das NBC TA 200–600.

**4. O que este dossiê fornece**

Este trabalho tem nível de asseguração **nenhum**. Ele aplica a metodologia das NBC TA a documentos públicos e a dados sintéticos, para fins de aprendizagem. Faltam três condições de um trabalho de asseguração: contratação pela parte responsável, acesso a registros (NBC TA 210 item 6(b)(iii)) e independência verificada por uma firma. Por isso, nenhuma conclusão aqui deve ser lida como opinião ou conclusão de auditor.
""",
evidencias="DF25 p. 26–32, 45; ITR3T25 p. 14–15; NORMAS (EC) p. 3–28. Referências cruzadas: PT 200 (segurança razoável), PT 210 (precondições), PT 260 (usuários e governança), PT 600 (perímetro do grupo).",
resultados="Sem exceções. O trabalho real é de asseguração razoável, com conclusão positiva e sem modificação. A revisão de ITR é de asseguração limitada (contraste documentado com fontes reais).",
conclusao="A auditoria das DF 2025 da CPFL tem os cinco elementos da EC e corresponde a asseguração razoável. Este dossiê reproduz a metodologia, mas não fornece asseguração.",
limitacoes="A lista de usuários é inferida do destinatário do relatório e do perfil acionário. A existência de trabalhos de asseguração não financeira contratados pela CPFL não foi verificada. O consolidado de normas contém comentários didáticos ('Comentado [LF…]') que não foram tratados como requisitos.",
))

# --------------------------------------------------------------------------- 200
PTS.append(dict(
codigo="PT 200", titulo="Objetivos gerais do auditor, ética, ceticismo, julgamento e risco de auditoria",
norma="NBC TA 200 (R1) (DOU 05/09/2016; NORMAS p. 29–56). Itens: 3, 5, 11, 13 (definições, inclusive risco de auditoria e risco de detecção), 14 (ética e independência), 15 (ceticismo), 16 (julgamento), 17 (evidência e risco de auditoria), A14–A52.",
objetivo="Documentar como os objetivos gerais do auditor (item 11) se aplicam a uma auditoria das DF consolidadas 2025 da CPFL. Mostrar ceticismo e julgamento aplicados neste trabalho, com exemplos concretos, e as condições, ausentes aqui, para obter segurança razoável.",
conta="Demonstrações contábeis consolidadas 2025 como um todo.",
afirmacoes="Riscos gerais identificados nas fontes: (R-G1) estimativas complexas — ativo financeiro da concessão (VNR), ativo contratual e receita não faturada (PAA, DF25 p. 27–29); (R-G2) julgamento sobre bifurcação de ativos da concessão (DF25 p. 29); (R-G3) dependência de dados de TI na receita não faturada (DF25 p. 28). O detalhamento por afirmação será feito no PT 315.",
populacao="NORMAS p. 29–56; DF25 p. 26–36, 68; controles do projeto (CPFL_B01_Controles_Execucao.xlsx, abas Divergencias e Conferencia_DF25).",
procedimentos=[
 ("200-01","Mapear os objetivos do item 11 para o caso CPFL","Realizado com evidência pública"),
 ("200-02","Registrar exigências éticas e de independência (item 14) e o que se pode verificar publicamente","Realizado com evidência pública"),
 ("200-03","Documentar aplicações reais de ceticismo neste trabalho (item 15)","Realizado com evidência pública"),
 ("200-04","Documentar julgamentos significativos já feitos (item 16)","Realizado com evidência pública"),
 ("200-05","Decompor o risco de auditoria (itens 13 e 17) para as áreas mais relevantes, de forma qualitativa","Planejado por falta de acesso (risco de controle não testável)"),
 ("200-06","Obter declaração de independência do preparador","Realizado com evidência pública — complementado por autodeclaração do aluno (22/10/2026)"),
],
corpo="""
**1. Objetivos gerais (item 11) aplicados**

(a) Obter segurança razoável de que as DF consolidadas estão livres de distorção relevante, por fraude ou erro. A base de mensuração é a materialidade do PT 320, sobre lucro antes dos tributos de R$ 8.091.246 mil (DF25 p. 36/4).
(b) Emitir relatório conforme as constatações. **No dossiê, não há emissão de opinião** (PT EC, seção 4).

**2. Ética e independência (item 14)**

| Aspecto | Trabalho real | Este dossiê |
|---|---|---|
| Declaração de independência | A PwC declara-se independente segundo o Código de Ética Profissional do Contador e as normas do CFC para entidades de interesse público (DF25 p. 26) | **Declaração do preparador (22/10/2026): não possui nenhum vínculo com o Grupo CPFL**, inclusive ações CPFE3, emprego, parentesco ou prestação de serviços. Trata-se de autodeclaração, não verificada externamente |
| Confidencialidade | Aplicável a informações do cliente | Só há dados públicos e sintéticos. Nada confidencial foi usado |
| Comunicação externa | — | Nenhum contato com a companhia, auditores ou terceiros (enunciado, seção 1) |

**3. Ceticismo profissional (item 15): exemplos reais neste trabalho**

1. Os valores do controle do projeto (fonte secundária) foram reconferidos na imagem do balanço. Foram achados **4 erros de transcrição**: DV01 (129.659), DV11 (715.764), DV12 (985.664) e DV13 (10.778.490), todos na DF25 p. 34–36.
2. Os arquivos-fonte não foram aceitos só por estarem legíveis. O FR 2025, o FR 2026 e o ITR 2T25 têm tamanhos exatos de 16 MiB e 8 MiB. O texto do FR 2025 termina no item 2.1, o que indica corte (DV15).
3. A versão das normas não foi presumida. A NBC TA 240 (R2) e a NBC TA 570 (R1), publicadas em 2026, foram afastadas para 2025 (DV09).
4. A conciliação aritmética da base sintética não é tratada como prova de valor justo (VNR).

**4. Julgamentos significativos já feitos (item 16)**

Os julgamentos registrados até aqui são:

- perímetro consolidado (D-B01-01);
- conta da base: ativo financeiro da concessão, 36,5% do ativo (DF25 p. 34/2);
- base de entrega reproduzida pelo gerador (D-B01-03);
- versões normativas (D-B01-02).

Cada julgamento tem fundamento registrado em DECISOES.md.

**5. Risco de auditoria (itens 13 e 17): leitura qualitativa**

| Área | Risco inerente | Risco de controle | Risco de detecção requerido | Base |
|---|---|---|---|---|
| Ativo financeiro da concessão (VNR) | Alto (estimativa, julgamento, PAA 3) | Não avaliável: sem acesso; assumido alto para fins didáticos | Baixo: exige substantivos extensos | DF25 p. 29, 68 |
| Receita não faturada (R$ 1.763.858 mil) | Alto (dados de TI, perdas técnicas e comerciais) | Não avaliável | Baixo | DF25 p. 28 |
| Ativo contratual (transmissão) | Alto (taxa de desconto, margens) | Não avaliável | Baixo | DF25 p. 27 |
| Caixa e equivalentes (R$ 2.229.320 mil) | Baixo | Não avaliável | Moderado | DF25 p. 34 |

A avaliação final de risco inerente e de controle, com o espectro de risco da NBC TA 315 (R2), fica no PT 315.

**6. Condições para segurança razoável e limitações inerentes (item 5)**

Uma auditoria real exige acesso a registros e pessoas, teste de controles e evidência externa (confirmações). Nada disso existe aqui. A evidência disponível é pública, majoritariamente documental de origem da própria entidade, e persuasiva, não conclusiva (item 5).
""",
evidencias="NORMAS p. 29–56; DF25 p. 26–29, 34–36, 68; Controles B01 (abas Divergencias, Mapa_Normativo); DECISOES.md. Referências cruzadas: PT 315 (riscos), PT 320 (materialidade), PT 220 (qualidade), PT 230 (registro de divergências).",
resultados="Quatro erros de transcrição em fonte secundária, todos corrigidos. Arquivos-fonte com indício de truncamento: 3. O preparador declarou não ter vínculo com o Grupo CPFL (22/10/2026).",
conclusao="Os objetivos gerais e os princípios do item 14–17 foram aplicados ao caso e documentados com exemplos verificáveis. Não há condições para segurança razoável neste trabalho, que é exercício acadêmico.",
limitacoes="O risco de controle não foi avaliado (sem acesso). A independência baseia-se em autodeclaração. A classificação de risco é preliminar até o PT 315.",
))

# --------------------------------------------------------------------------- 210
PTS.append(dict(
codigo="PT 210", titulo="Concordância com os termos do trabalho — precondições e carta de contratação didática",
norma="NBC TA 210 (R1) (DOU 05/09/2016; NORMAS p. 57–88). Itens: 6 (condições prévias: estrutura aceitável e responsabilidades da administração), 7–8 (limitação de alcance; ausência de condições prévias), 9–10 (termos e conteúdo mínimo da carta), 13 (auditoria recorrente), A2–A27.",
objetivo="Avaliar, com informação pública, se as precondições de uma auditoria das DF 2025 da CPFL estariam presentes, e redigir uma minuta didática de carta de contratação com o conteúdo do item 10.",
conta="Contratação da auditoria das DF individuais e consolidadas de 2025.",
afirmacoes="Riscos: (R-210-1) estrutura de relatório inaceitável → baixo (CPC/IFRS aprovados pela CVM); (R-210-2) administração não reconhecer responsabilidades → sem indício (DF assinadas pela diretoria e pelo contador, DF25 p. 115); (R-210-3) limitação de acesso → **presente neste dossiê**, pois o aluno não tem acesso.",
populacao="DF25 p. 26, 45–46, 115; NORMAS p. 57–88.",
procedimentos=[
 ("210-01","Avaliar a aceitabilidade da estrutura (item 6(a)) com base na nota 2.1","Realizado com evidência pública"),
 ("210-02","Verificar indícios públicos do reconhecimento de responsabilidades pela administração (item 6(b))","Realizado com evidência pública"),
 ("210-03","Obter carta de contratação assinada e concordância da administração","Planejado por falta de acesso (não executável — não haverá envio)"),
 ("210-04","Redigir minuta didática com o conteúdo do item 10","Simulado para fins didáticos (documento-modelo, não enviado)"),
],
corpo="""
**1. Precondições (item 6)**

| Requisito | Evidência pública | Avaliação |
|---|---|---|
| (a) Estrutura aceitável | DF elaboradas conforme práticas contábeis adotadas no Brasil (CPC aprovados pela CVM) e IFRS do IASB (DF25 p. 45/13). Estrutura de propósito geral, exigida para companhia aberta | Aceitável |
| (b)(i) Responsabilidade pela elaboração | DF aprovadas pelo Conselho de Administração em 04/03/2026 e assinadas pela diretoria e pelo contador responsável (DF25 p. 45 e 115) | Indício favorável. Confirmação formal depende da carta (210-03) |
| (b)(ii) Controle interno | Relatório da PwC descreve avaliação de controles (DF25 p. 27–29) | Indício de existência; eficácia não verificável |
| (b)(iii) Acesso a informações e pessoas | Inexistente para o aluno | **Precondição não atendida neste dossiê.** Em trabalho real, impediria a aceitação (itens 7–8) |

**2. Auditoria recorrente (item 13)**

A PwC já revisava os ITR de 2025 (ITR3T25 p. 14–15), o que indica relação recorrente. Para este dossiê, o caso é tratado como **auditoria inicial didática** (PT 510), conforme o enunciado.

**3. Minuta didática de carta de contratação**

> **MINUTA DIDÁTICA — NÃO ENVIADA — SEM ASSINATURAS — PREPARADA PARA FINS ACADÊMICOS (UnB, Auditoria 1)**
>
> Aos Administradores e ao Conselho de Administração da CPFL Energia S.A.
>
> **Objetivo e alcance (item 10(a)).** Auditoria das demonstrações contábeis individuais e consolidadas de 31/12/2025, conforme as normas brasileiras e internacionais de auditoria. O objetivo é expressar opinião sobre se elas apresentam adequadamente, em todos os aspectos relevantes, a posição patrimonial e financeira, o desempenho e os fluxos de caixa.
>
> **Responsabilidades do auditor (item 10(b)).** Obter segurança razoável, não absoluta, de que as demonstrações estão livres de distorção relevante, por fraude ou erro. Planejar e executar a auditoria com ceticismo e julgamento profissional. Comunicar à governança os assuntos exigidos pela NBC TA 260 e deficiências significativas (NBC TA 265). Existe risco inevitável de que distorções relevantes não sejam detectadas, por causa das limitações inerentes.
>
> **Responsabilidades da administração (item 10(c)).** Elaborar as demonstrações conforme as práticas contábeis adotadas no Brasil e as IFRS. Manter o controle interno necessário. Dar acesso irrestrito a registros, documentação e pessoas, e fornecer representações formais por escrito (NBC TA 580).
>
> **Estrutura aplicável (item 10(d)).** Práticas contábeis adotadas no Brasil (CPC/CVM) e IFRS emitidas pelo IASB.
>
> **Forma e conteúdo esperados do relatório (item 10(e)).** Relatório do auditor independente com opinião e base para opinião, seção de Principais Assuntos de Auditoria (companhia listada) e responsabilidades. A forma e o conteúdo podem mudar conforme as constatações.
>
> Local/data: ____ · Auditor: ____ · Administração: ____ (campos deliberadamente em branco)
""",
evidencias="DF25 p. 26–29, 45, 115; ITR3T25 p. 14–15; NORMAS p. 57–88. Referências cruzadas: PT EC (partes), PT 260, PT 265, PT 510 (auditoria inicial), PT 580 (representações).",
resultados="As precondições (a), (b)(i) e (b)(ii) têm indícios favoráveis em fontes públicas. A precondição (b)(iii), acesso, não é atendida no contexto acadêmico.",
conclusao="Em um trabalho real, as precondições pareceriam atendidas, sujeitas à confirmação formal. Neste dossiê, a ausência de acesso é a limitação estrutural que leva vários procedimentos à modalidade 'planejado'.",
limitacoes="Não houve contato nem obtenção de concordância. A minuta é modelo didático. Honorários, prazos e equipe não foram definidos porque não há contratação real.",
))

# --------------------------------------------------------------------------- 220
PTS.append(dict(
codigo="PT 220", titulo="Gestão da qualidade no nível do trabalho",
norma="NBC TA 220 (R3) (DOU 09/12/2021; aplicável a períodos iniciados a partir de 01/01/2023 — item 10, NORMAS p. 93). Itens: 11 (objetivo), 13 (responsabilidade do sócio), 16–21 (ética), 22–24 (aceitação), 25–28 (recursos), 29–34 (direção, supervisão e revisão), 35 (consulta), 36 (revisão de qualidade do trabalho), 37–38 (diferenças de opinião), 39 (monitoramento), 40 (responsabilidade geral), 41 (documentação).",
objetivo="Planejar a gestão da qualidade deste trabalho: direção, supervisão, revisão, consultas e recursos. Identificar conflitos e riscos à qualidade, distinguindo a estrutura de uma firma real da estrutura efetivamente disponível neste trabalho individual.",
conta="Processo de elaboração do dossiê (todos os PTs).",
afirmacoes="Riscos à qualidade identificados (ver matriz abaixo). São riscos do processo do trabalho, não afirmações de DF.",
populacao="NORMAS p. 89–130; controles do projeto (ESTADO_DO_PROJETO.md, DECISOES.md, PENDENCIAS.md, aba Divergencias).",
procedimentos=[
 ("220-01","Definir papéis: 'sócio do trabalho' = aluno; equipe = aluno + ferramenta de IA como recurso tecnológico","Realizado com evidência pública"),
 ("220-02","Montar matriz de riscos à qualidade e respostas","Realizado com evidência pública"),
 ("220-03","Executar revisão automatizada por bloco e revisão técnica transversal (Bloco 12)","Realizado com evidência pública — revisões automatizadas RV-B01 a RV-B12 registradas (seção 3–5)"),
 ("220-04","Registrar validações do aluno sobre decisões materiais","Realizado com evidência pública — D-B01-02 e D-B01-03 validadas em 22/10/2026"),
 ("220-05","Revisão de qualidade do trabalho (item 36) por revisor independente","Planejado por falta de acesso: não há revisor; campo em branco"),
 ("220-06","Consultas (item 35) ao professor sobre dúvidas de escopo","Planejado por falta de acesso — consulta opcional ao professor não realizada (PB03-02)"),
],
corpo="""
**1. Estrutura: firma real × este trabalho**

| Elemento (NBC TA 220 R3) | Firma de auditoria real | Este dossiê |
|---|---|---|
| Sócio do trabalho (item 13) | Sócio responsável, com a liderança da qualidade | Aluno (matrícula 231020069) assume a responsabilidade |
| Equipe e recursos (itens 25–28) | Equipe multidisciplinar, especialistas de TI e avaliação (a PwC usou especialistas de TI, DF25 p. 28) | Aluno + IA como recurso tecnológico. **Sem especialista** em avaliação de VNR nem em TI |
| Direção, supervisão e revisão (itens 29–34) | Revisão hierárquica dos papéis | Revisão automatizada ao fim de cada bloco + validação do aluno nas decisões materiais |
| Consulta (item 35) | Departamento técnico | Professor da disciplina (planejado) |
| Revisão de qualidade (item 36) | Revisor de qualidade designado pela firma, normalmente exigido para companhias listadas | **Inexistente.** Não será simulada |
| Diferenças de opinião (37–38) | Políticas da firma | Registro em DECISOES.md; prevalece o enunciado do professor |
| Monitoramento (item 39) | Sistema de gestão da qualidade da firma | Não aplicável a trabalho individual. Analisado e documentado aqui |

**2. Matriz de riscos à qualidade (com evidência de ocorrência)**

| ID | Risco à qualidade | Ocorreu? | Resposta |
|---|---|---|---|
| RQ1 | Usar fonte secundária com erro | **Sim**: 4 erros no controle antigo (DV01, DV11–DV13) | Reconferir todo valor na imagem da DF; somas por fórmula |
| RQ2 | Usar arquivo-fonte corrompido ou truncado | **Sim**: FR 2025 e 2026 (DV15); suspeita no ITR 2T25 | Verificar tamanho e fim do texto antes de citar; registrar limitação |
| RQ3 | Aplicar versão normativa errada | **Evitado**: 240 (R2) e 570 (R1) de 2026 | Mapa normativo com vigência lida no texto |
| RQ4 | IA afirmar fato, página ou item inexistente | Risco permanente | Toda afirmação com documento e página; itens conferidos no texto; revisão no B12 |
| RQ5 | Apresentar simulação como fato da CPFL | Risco permanente | Modalidade por procedimento; rótulo SINTÉTICO na base |
| RQ6 | Contaminar os testes com o gabarito | Risco permanente | Gabarito em pasta reservada, não aberto antes do congelamento (PT 530) |
| RQ7 | Prazo curto (entrega em 25/10/2026) | Sim | Cronograma por blocos; prioridade a requisitos obrigatórios |
| RQ8 | Conflito de interesse do preparador | Desconhecido | Declaração do aluno (PT 200) |

**3. Registro de revisões realizadas até agora**

- RV-B01: revisão automatizada. Somas recalculadas e vigências lidas. Resultado: DV01–DV11.
- RV-B02: revisão automatizada. 7 conciliações por fórmula e 92 fórmulas sem erro. Resultado: DV12–DV15.
- Validação do aluno: D-B01-02 e D-B01-03 (22/10/2026).

**4. Atualização em 23/10/2026 (Bloco 11): revisões dos Blocos 03 a 11**

| Ref. | Tipo | O que foi conferido | Resultado |
|---|---|---|---|
| RV-B03 | Automatizada | Campos obrigatórios dos PTs; citações de página na NBC TA | Sem campo vazio |
| RV-B04 | Automatizada | Fórmulas de materialidade e da matriz de riscos | 0 erros de fórmula; NBC TA 500 item 9 corrigido para p. 449 |
| RV-B05 | Automatizada | Mapa do grupo e segmentos × LAIR | Diferença zero (DV18) |
| RV-B06 | Automatizada | Saldos por distribuidora nas DFs individuais | DV19 (proporções hipotéticas da base v1) |
| RV-B07 | Automatizada | 16 verificações da base; reprodução em pasta limpa | 0 falhas; 4 hashes idênticos |
| RV-B08 | Automatizada | Pré-registro e congelamento antes do gabarito (horários do Drive) | Protocolo cumprido; comparação só após o congelamento |
| RV-B09 | Automatizada | 61 linhas de abertura; planilha | 0 diferenças; DV20 (relatório de 2024 ausente do PDF) |
| RV-B10 | Automatizada | Movimentação das provisões; quadro de liquidez | Total de debêntures registrado como 30.641.582 (erro, corrigido para 30.641.585 no RV-B12) |
| RV-B11 | Automatizada | Consolidação do PT 450 igual ao PT 530; planilha B11 | 0 erros de fórmula |
| RV-B12 | Automatizada (segunda leitura crítica, Bloco 12) | Cobertura do enunciado; 27 PTs × 9 campos; 143 modalidades; citações item × página; números × páginas da DF25; reprodução da base e dos testes em pasta limpa; eventos subsequentes; varredura de afirmações indevidas | 14 achados no registro de revisão (CPFL_B12_Revisao_Tecnica_Cobertura.xlsx); erros comprovados corrigidos na v0.9 |

**Validações do aluno:** D-B04-01 (materialidade), declaração de independência (PT 200), D-B06-01 e D-B06-02 (base v2), em 22 e 23/10/2026.

**Limite.** Todas as revisões RV foram feitas pela mesma IA que preparou os PTs. Valem como autoconferência, não como revisão independente (itens 29–34). O campo 9 de cada PT continua em branco para o revisor humano.

Nenhuma revisão de terceiros foi realizada ou simulada.
""",
evidencias="NORMAS p. 89–130; DF25 p. 28; ESTADO_DO_PROJETO.md; DECISOES.md; aba Registro_Revisao (Controles B01). Referências cruzadas: PT 200 (ceticismo), PT 230 (documentação), PT 530 (blindagem do gabarito), Bloco 12.",
resultados="Três riscos à qualidade já se materializaram (RQ1, RQ2, RQ7) e foram tratados. Não há revisor de qualidade independente.",
conclusao="A qualidade é gerida com controles proporcionais a um trabalho individual. As lacunas em relação a uma firma real (especialistas, revisor de qualidade, monitoramento) estão documentadas e limitam as conclusões.",
limitacoes="A revisão por IA não substitui revisão humana independente. A página 100 do PDF do consolidado de normas (NBC TA 220) está quase vazia; os itens citados foram lidos em outras páginas, e a lacuna está registrada (PB01-07).",
))

# --------------------------------------------------------------------------- 230
PTS.append(dict(
codigo="PT 230", titulo="Documentação de auditoria — índice, códigos, referências, versões, montagem e guarda",
norma="NBC TA 230 (R1) (DOU 05/09/2016; NORMAS p. 131–145). Itens: 7 (tempestividade), 8 (suficiência para auditor experiente), 9 (identificação de itens testados, quem executou e quando, quem revisou), 11 (inconsistências), 12 (não atendimento de requisito), 14–16 (montagem e alterações posteriores), A21 e A23 (prazos de referência).",
objetivo="Estabelecer o sistema de documentação do dossiê: índice, convenção de códigos e marcas, referências cruzadas, controle de versões e regras de montagem e guarda.",
conta="Arquivo do trabalho (dossiê, planilhas, base, códigos e controles).",
afirmacoes="Riscos: documentação insuficiente para um revisor experiente entender o que foi feito (item 8); perda de rastreabilidade entre versões; alteração não registrada após a montagem (item 16).",
populacao="Todos os arquivos do projeto no Drive (pasta 09_Elaboracao_do_trabalho_CPFL e TRABALHO FINAL) e no futuro repositório GitHub.",
procedimentos=[
 ("230-01","Definir índice e convenção de códigos","Realizado com evidência pública"),
 ("230-02","Definir legenda de marcas e forma de referência cruzada","Realizado com evidência pública"),
 ("230-03","Instituir controle de versões (sufixos _vN e _historico; hashes SHA-256)","Realizado com evidência pública — aplicado em DECISOES, ESTADO e PENDENCIAS"),
 ("230-04","Definir montagem final e guarda (prazo e local)","Realizado com evidência pública — regras definidas; montagem final registrada no Bloco 13"),
],
corpo="""
**1. Índice do arquivo (estrutura de pastas)**

| Pasta | Conteúdo |
|---|---|
| 00_Controle | ESTADO_DO_PROJETO, DECISOES, PENDENCIAS, controles do B01 (inventário, cobertura, mapa normativo) |
| 01_Dados_reais | Dados transcritos da DF25 com página; memorando da entidade |
| 02_Planejamento | Materialidade, riscos, plano e programas (B04–B05) |
| 03_Base_sintetica | Base, dicionário, gerador, parâmetros (SINTÉTICO) |
| 04_Testes | Seleções, resultados, comparação com gabarito (após congelamento) |
| 05_Papeis | Fontes em texto dos PTs |
| 06_Dossie | Dossiê consolidado DOCX/PDF (versões) |
| 07_Entrega | Pacote final para o GitHub |
| TRABALHO FINAL | Dossiê consolidado vigente e arquivos de entrega (escolha do aluno) |

**2. Convenção de códigos**

- **PT nnn**: papel de trabalho da norma correspondente (PT EC, PT 200 … PT 600). Programas por ciclo: **PG-REC** (receitas), **PG-DISP** (disponibilidades), **PG-EST** (estoques), **PG-IMOB** (imobilizado), **PG-PASS** (passivos) e **PG-ESTIM** (estimativas).
- Procedimentos: **[PT]-nn** (ex.: 210-03). Divergências: **DVnn**. Decisões: **D-Bnn-nn**. Pendências: **PBnn-nn**. Fontes: **Fnn/FCnn** (preservam os IDs da etapa 5).
- Citação de fonte: documento + página física/página impressa (ex.: DF25 p. 34/2).

**3. Legenda de marcas**

| Marca | Significado |
|---|---|
| ✓ | Conferido com a fonte original (documento e página) |
| Σ | Soma recalculada por fórmula |
| ⇄ | Conciliado com outra demonstração ou nota |
| [P] | Procedimento planejado por falta de acesso |
| [S] | Simulado: dado sintético, não é da CPFL |
| [Pub] | Realizado com evidência pública |

**4. Referências cruzadas.** Cada PT tem o campo "Evidências e referências cruzadas", que remete a outros PTs e a abas de planilhas (ex.: CPFL_B02_Dados_Reais_2025.xlsx › Conciliacoes › CC05).

**5. Controle de versões**

- Arquivos substituídos não são apagados: são renomeados com sufixo `_vN_..._historico`. Exemplo: DECISOES_v1_2026-10-22_historico.md.
- Fontes centrais têm SHA-256 registrado. Exemplos: DF25 0694f2b9…a578 e consolidado de normas f2edf5fa…2775.
- O dossiê consolidado é versionado por bloco (v0.1 = Bloco 03).

**6. Montagem e guarda**

| Aspecto | Exigência ou referência normativa | Escolha deste projeto |
|---|---|---|
| Tempestividade (item 7) | Documentar tempestivamente | Documentação ao fim de cada bloco, com data |
| Montagem (item 14 e A21) | Montagem tempestiva após a data do relatório. A21 indica, como referência, prazo que geralmente não ultrapassa 60 dias | Montagem final em 25/10/2026 (Bloco 13), data da entrega |
| Guarda (item 15 e A23) | Não descartar antes do fim do período de guarda. A23 cita, como referência, período geralmente não inferior a 5 anos | Repositório GitHub + Drive institucional. Prazo de guarda: definido pelo aluno e pela disciplina (não normativo) |
| Alterações após montagem (item 16) | Documentar quando, por quem e por quê | Novo commit/versão com nota de alteração; versão anterior preservada |

Os itens A21 e A23 remetem a uma norma de controle de qualidade da firma (NBC PA 01, conforme o texto do consolidado). Os prazos acima são **referências do material explicativo**, não escolhas obrigatórias deste trabalho acadêmico.
""",
evidencias="NORMAS p. 131–145; estrutura do Drive (verificada em 22/10/2026); DECISOES.md (versionamento). Referências cruzadas: PT 220 (revisões), Matriz de cobertura (Controles B01).",
resultados="Sistema de documentação definido e já aplicado: versões históricas preservadas e hashes registrados. Os itens 11 e 12 foram aplicados ao registrar divergências (DV01–DV15) e procedimentos não executáveis (modalidade 'planejado').",
conclusao="A documentação permite a um revisor experiente rastrear fonte → procedimento → resultado. A montagem final e a guarda ficam para o Bloco 13.",
limitacoes="O Drive não registra hash automaticamente; a integridade depende dos hashes calculados nas sessões de trabalho. A versão vigente da norma de qualidade da firma citada em A21/A23 não foi conferida.",
))

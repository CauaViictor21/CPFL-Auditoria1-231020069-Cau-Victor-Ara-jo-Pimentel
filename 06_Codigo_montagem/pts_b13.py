# -*- coding: utf-8 -*-
"""Bloco 13: versão final. Campo 10 (requisito × orientação × julgamento) por PT, programa PG-CONS,
atualizações finais de PTs e textos das Partes A, B, E, F e G do dossiê."""
DATA = "24/10/2026"
PTS = []

# Campo 10 — o que a norma EXIGE (requisito), o que é material de aplicação/explicativo (orientação, itens A)
# e o que é escolha do preparador (julgamento). Itens conforme o campo 1 de cada PT.
RJ = {
 "PT EC": ("Elementos de um trabalho de asseguração e distinção entre asseguração razoável e limitada (EC itens 12–16 e 26–27).", "Exemplos de trabalhos e de objetos (EC, texto explicativo).", "Tratar o dossiê como exercício sem asseguração; usar a auditoria real só como referência de forma."),
 "PT 200": ("Cumprir exigências éticas, ceticismo, julgamento, evidência apropriada e suficiente e todas as NBC TA relevantes (itens 14–24).", "A20–A76 (riscos inerentes, limitações inerentes, papel do julgamento).", "Independência apoiada em autodeclaração do aluno (D-B05-02); classificação preliminar de riscos."),
 "PT 210": ("Verificar estrutura de relatório aceitável e reconhecimento das responsabilidades da administração (item 6) e formalizar os termos (itens 9–12).", "Exemplo de carta de contratação do apêndice (forma, não conteúdo obrigatório).", "Minuta de termos só didática; falta de acesso tratada como limitação estrutural, não como recusa da administração."),
 "PT 220": ("Responsabilidade pela qualidade, direção, supervisão, revisão e documentação no nível do trabalho (itens 13, 29–34, 41).", "Material de aplicação sobre natureza e extensão da revisão.", "Revisões automatizadas registradas (RV-B01 a RV-B12) e campo de revisão humana em branco; nenhuma revisão de terceiros simulada."),
 "PT 230": ("Documentação tempestiva, suficiente para auditor experiente, com itens testados, preparador e revisor (itens 7–9) e montagem final (itens 14–16).", "Prazo de referência de 60 dias para montagem (A21) e de guarda (A23).", "Codificação PT/DV/FC/D/RV, controle de versões e estrutura de pastas do repositório."),
 "PT 240": ("Presunção de risco de fraude na receita e risco de burla de controles pela administração; respostas aos riscos avaliados (itens 26–33).", "Fatores de risco de fraude do apêndice 1 (exemplos).", "Classificação de R16 como significativo e foco na receita não faturada e nas estimativas da concessão."),
 "PT 250": ("Obter entendimento da estrutura legal e evidência sobre leis de efeito direto (itens 13–15).", "Exemplos de leis e regulamentos (A-itens).", "Seleção ANEEL, tributos e CVM como normas de efeito direto relevantes."),
 "PT 260": ("Comunicar responsabilidades, alcance e época, constatações significativas e independência (itens 14–17), por escrito quando significativas (item 19).", "Exemplos de assuntos a comunicar e forma (A-itens).", "Minuta única para o Comitê de Auditoria e o Conselho, sem nomes de pessoas, não enviada."),
 "PT 265": ("Determinar deficiências e se são significativas; comunicar por escrito as significativas (itens 7–9, 11).", "Indicadores de deficiência significativa (A5–A7).", "Separar real, hipótese, sintético e falta de acesso (D-B11-01, D-B11-02)."),
 "PT 300": ("Estratégia global e plano de auditoria, atualizados quando necessário (itens 7–10).", "Considerações sobre o plano e a natureza do trabalho.", "Abordagem predominantemente substantiva e programas por ciclo."),
 "PT 315": ("Identificar e avaliar riscos de distorção relevante nos níveis das DF e das afirmações, com fatores de risco inerente (itens 12, 19–34).", "Espectro de risco inerente e exemplos de fatores (apêndices).", "Matriz de 19 riscos; R01, R02, R03 e R16 como significativos."),
 "PT 320": ("Determinar materialidade global, de execução e específicas e revisá-las (itens 10–14).", "Referenciais e percentuais exemplificativos (A3–A13).", "5% do LAIR, execução de 75% e trivial de 5% (D-B04-01, validada pelo aluno)."),
 "PT 330": ("Respostas gerais e procedimentos adicionais por afirmação; procedimentos substantivos para riscos significativos (itens 5–7, 18–21); avaliar suficiência (itens 25–27).", "Natureza, época e extensão (A-itens).", "Sem teste de controles, ênfase substantiva; procedimentos dependentes de acesso classificados como planejados."),
 "PT 402": ("Entender os serviços da organização prestadora e responder aos riscos (itens 9–16).", "Tipos de relatório de asseguração (A-itens).", "Identificação de previdência e liquidação de energia como serviços relevantes."),
 "PT 450": ("Acumular distorções não triviais, comunicá-las e avaliar se são relevantes, individualmente ou em conjunto (itens 5–11).", "Tipos de distorção — factual, de julgamento, projetada (A6).", "Hipóteses não acumuladas; distorção sintética acumulada só na simulação (D-B11-01)."),
 "PT 500": ("Definir procedimentos apropriados e avaliar relevância e confiabilidade da informação usada como evidência (itens 6–9, 11).", "Fontes e tipos de evidência (A1–A60).", "Escala S/P/I de suficiência por risco; base sintética só como demonstração de método."),
 "PT 501": ("Procedimentos para estoques relevantes, litígios e segmentos (itens 4–13).", "Exemplos de procedimentos e de carta jurídica (A-itens).", "Aplicabilidade limitada para estoques; carta jurídica só como modelo."),
 "PT 505": ("Manter controle sobre as solicitações de confirmação e avaliar respostas (itens 7–16).", "Uso de confirmação negativa e meios eletrônicos (A-itens).", "Critérios de seleção didáticos; nenhuma confirmação enviada."),
 "PT 510": ("Obter evidência de que os saldos iniciais não contêm distorção e de consistência das políticas (itens 5–9).", "Procedimentos possíveis quando houve auditor anterior (A-itens).", "Tratamento como auditoria inicial didática; opinião de 2024 inferida de documentos indiretos (DV20)."),
 "PT 520": ("Adequação, confiabilidade dos dados, expectativa e limite em analíticos substantivos (item 5); revisão analítica final (item 6); investigação (item 7).", "Precisão da expectativa e fatores (A-itens).", "Modelo de expectativa do VNR e limite de 30% da execução (D-B09-01)."),
 "PT 530": ("Desenho da amostra, tamanho, seleção, natureza das distorções, projeção e avaliação (itens 6–15).", "Fatores que afetam o tamanho e métodos de seleção (A10–A23, apêndices).", "MUS com parâmetros pré-registrados e ampliação residual (D-B08-01, D-B08-02)."),
 "PT 540": ("Entender a estimativa, avaliar riscos e responder a método, premissas e dados; revisão retrospectiva (itens 13–32).", "Exemplos de incerteza de estimativa e de indicadores de viés (A-itens).", "Não desenvolver estimativa pontual do auditor sem base homologada (D-B09-02)."),
 "PT 550": ("Entender relações e transações com partes relacionadas e responder aos riscos (itens 11–25).", "Alertas de partes não identificadas (A-itens).", "R13 moderado; completude dependente de acesso."),
 "PT 560": ("Procedimentos até a data do relatório e reação a fatos conhecidos depois (itens 6–17).", "Exemplos de eventos que originam ou não ajuste (A-itens).", "Corte de pesquisa em 23/10/2026 (D-B12-02); renovação tratada como evento de 2026 (D-B09-03)."),
 "PT 570": ("Avaliar eventos e condições, a avaliação da administração por ao menos 12 meses e concluir sobre incerteza relevante (itens 10–25, versão de 2016).", "Exemplos de eventos e fatores atenuantes (A-itens).", "Não concluir pelo cumprimento de covenants sem definições contratuais."),
 "PT 580": ("Solicitar representações de quem tem responsabilidade pelas DF; data não posterior à do relatório (itens 9–15); avaliar confiabilidade (itens 16–20).", "Exemplo de carta do apêndice.", "Minuta sem data e sem assinatura; signatários por cargo (D-B11-03)."),
 "PT 600": ("Responsabilidade pela direção do trabalho do grupo, componentes, materialidade de componentes e consolidação (itens 13–49).", "Exemplos de componentes significativos (A-itens).", "Materialidade de componentes de 70%/50% da execução (D-B05-01)."),
}

PG_CONS = """## PG-CONS — Programa de auditoria: Consolidação e grupo

**Riscos:** R14, R13, R16 · **Base:** consolidado de 81.099.930 (BP p. 34/2); segmentos (nota 30, p. 103/71); estrutura do grupo (nota 1) · **Aplicabilidade:** Aplicável — grupo com distribuidoras, geração, transmissão e comercialização; reorganizações em 2025–2026 · **Ligação:** PT 600, PT 550, PT 501

| Nº | Procedimento e modalidade |
|------------|----------------------------------------------------------------------------------------|
| 1 | Mapear o perímetro de consolidação e o método por investida (nota 1 e nota 13) [Pub] — PT 600 |
| 2 | Conciliar o LAIR dos segmentos com o consolidado (nota 30) [Pub — feito no B05, DV18] — PT 501/600 |
| 3 | Conferir o saldo consolidado do ativo financeiro da concessão com a soma das distribuidoras (DFs individuais, nota 11) [Pub — B06] — PT 500 |
| 4 | Conferir os demonstrativos consolidados com a base da CVM (DFP 2025, versão 1) [Pub — B13] — seção 3.2 |
| 5 | Testar eliminações intragrupo (vendas entre segmentos e mútuos) com balancetes dos componentes [P] — PT 600 |
| 6 | Enviar instruções aos auditores de componentes e avaliar seus relatórios [P] — PT 600 |
| 7 | Avaliar o julgamento de controle conjunto das investidas e efeitos das reorganizações de 2026 [Pub/P] — PT 600/560 |

Preparador: Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas — 24/10/2026. Revisão: ____ (em branco).
"""

ADD_260 = """
**4. Atualização em 24/10/2026 (Bloco 13): estrutura de governança confirmada na base da CVM**

O arquivo de pareceres e declarações da DFP 2025 na CVM (dfp_cia_aberta_parecer_2025, versão 1) contém, além do relatório do auditor:

- relatório anual resumido do **Comitê de Auditoria**, com três membros independentes, datado de 27/02/2026;
- **parecer do Conselho Fiscal**, de 27/02/2026, que menciona o relatório da PwC sem ressalvas datado de 04/03/2026;
- declarações da diretoria sobre as DF e sobre o relatório do auditor.

Com isso, o subgrupo pretendido para a comunicação (item 13) é o **Comitê de Auditoria**, com cópia ao Conselho de Administração e ao Conselho Fiscal. A limitação do FR truncado (DV15) fica superada para este ponto. Nomes de pessoas não foram transcritos.
"""

ADD_500 = """
**9. Atualização em 24/10/2026 (Bloco 13): conferência DF25 (PDF) × base de dados da CVM**

Fonte: dados abertos da CVM, DFP 2025, versão 1, documento 155108, recebido em 05/03/2026 (arquivos BPA, BPP e DFC-MI consolidados, filtrados pelo CNPJ 02.429.144/0001-93; escala MIL). Detalhe na seção 3.2 do dossiê.

| Resultado | Quantidade |
|---|---:|
| Valores transcritos do PDF (BP e DFC, 2025 e 2024) comparados | 182 |
| Idênticos na CVM | 168 |
| Diferença de ±1 ou ±2 (arredondamento, nota 2.4) | 8 |
| Agregação diferente de contas no modelo da CVM (soma confere ±1) | 4 |
| Subtotal derivado da DFC (6.01.01 + 6.01.02 confere) | 2 |
| **Diferenças sem explicação** | **0** |

A fonte de maior confiabilidade disponível (dados oficiais da CVM) corrobora a transcrição das demonstrações. A DRE consolidada da CVM não pôde ser lida (arquivo acima do limite de leitura); o LAIR de 8.091.246 confere pela DFC (6.01.01.01).
"""

ADD_230 = """
**4. Montagem final (Bloco 13, 24/10/2026)**

- Versão final do dossiê: **v1.0** (DOCX e PDF gerados do mesmo arquivo). Versões 0.1 a 0.9 preservadas no Drive (06_Dossie).
- Repositório de entrega organizado em pastas numeradas (Apêndice C) com README de reprodução.
- Após a montagem, alterações só com registro em DECISOES.md e nova versão (item 16).
"""

UPDATES = {
 "PT 260": dict(corpo_add=ADD_260, resultados_add=" Bloco 13: Comitê de Auditoria e Conselho Fiscal confirmados na base da CVM (pareceres de 27/02/2026).", evidencias_add=" Bloco 13: CVM, DFP 2025 v1 (dfp_cia_aberta_parecer_2025)."),
 "PT 500": dict(corpo_add=ADD_500, resultados_add=" Bloco 13: 182 valores do PDF conferidos com a CVM; 0 diferenças sem explicação.", evidencias_add=" Bloco 13: CVM, DFP 2025 v1, documento 155108 (BPA, BPP, DFC-MI consolidados)."),
 "PT 230": dict(corpo_add=ADD_230, conclusao="A documentação permite a um revisor experiente rastrear fonte → procedimento → resultado. A montagem final foi concluída no Bloco 13 (v1.0); alterações posteriores exigem nova versão registrada.", proc_fix={"230-04": "Realizado com evidência pública — montagem final v1.0 no Bloco 13"}),
}

# ---------------------------------------------------------------- Parte B (identificação e conferência CVM)
PARTE_B_ID = """## 3.1 Identificação da companhia atribuída

| Item | Dado | Fonte |
|---|---|---|
| Razão social | CPFL ENERGIA S.A. | CVM, dfp_cia_aberta_2025.csv (DENOM_CIA); DF25 p. 1 |
| CNPJ | 02.429.144/0001-93 | CVM (CNPJ_CIA); DF25 |
| Código CVM | 01866-0 (018660 nos dados abertos) | CVM (CD_CVM) |
| Negociação | CPFE3, segmento Novo Mercado da B3 | FR 2025, item 1.1 |
| Denominação anterior | "Draft II" (FR 2025 v6, item 1.1; grafia completa no cadastro CVM pendente — PB02-02) | FR 2025 |
| Documento examinado | DFP 2025, versão 1, documento 155108, recebido pela CVM em 05/03/2026 | CVM (VERSAO, ID_DOC, DT_RECEB) |
| Relatório do auditor | PwC, Campinas, 04/03/2026, classificado como "Sem Ressalva" | CVM (dfp_cia_aberta_parecer_2025, TP_RELAT_AUD); DF25 p. 26–32 |
| Governança que se manifestou sobre as DF | Comitê de Auditoria (relatório de 27/02/2026) e Conselho Fiscal (parecer de 27/02/2026) | CVM (dfp_cia_aberta_parecer_2025) |
| Aprovação | Autorização pela administração em 23/02/2026; aprovação pelo Conselho de Administração em 04/03/2026 | DF25 nota 2.1, p. 45 |

## 3.2 Conferência DF25 (PDF) × base de dados da CVM (Bloco 13)

**Procedimento [Pub].** Os 182 valores transcritos do PDF para a planilha do Bloco 02 (balanço ativo, balanço passivo e DFC, 2025 e 2024, inclusive totais divulgados) foram comparados, por programa, com os arquivos consolidados da DFP 2025 na CVM (BPA_con, BPP_con e DFC_MI_con, escala MIL, ordem ÚLTIMO = 2025 e PENÚLTIMO = 2024). Script: b13_conferencia_cvm.py; resultado: CPFL_B13_Conferencia_PDF_CVM.xlsx.

| Classe | Quantidade | Itens | Tratamento |
|---|---:|---|---|
| Idênticos | 168 | — | Conferido ⇄ |
| Arredondamento ±1/±2 | 8 | Outros ativos 2024; total do AC 2024; imobilizado 2025; intangível 2025; total do ANC 2024; total do PC 2025; reserva de lucros a realizar 2024; total do PL 2025 | Nota 2.4 (DF25 p. 46): arredondamento após totalização |
| Agregação diferente | 4 | Outras contas a pagar circulante e não circulante 2024; PL dos controladores 2025 e 2024 | O PDF agrega contas que a CVM separa (por exemplo, obrigações sociais + uso do bem público + taxas regulamentares + outras contas a pagar = 2.984.241 ≈ 2.984.242); PL dos controladores = 2.03 − 2.03.09 |
| Subtotal derivado | 2 | "Caixa líquido gerado pelas operações" 2025 e 2024 | = 6.01.01 + 6.01.02 da CVM |
| Sem explicação | **0** | — | — |

Limitação: a DRE consolidada da CVM (6,4 MB) não pôde ser lida pelo conector; o LAIR (8.091.246 e 8.088.893) confere pela DFC da CVM (conta 6.01.01.01). Ativo total de 81.099.930 e ativo financeiro da concessão de 29.623.619 conferem com a CVM (contas 1 e 1.02.01.10.08).
"""

PARTE_E_INTRO = """Base **SINTÉTICA** para fins didáticos [S]. Os registros **não** são dados internos da CPFL. Só o saldo total, os saldos por distribuidora e a natureza da conta são reais (DF25 p. 34/2 e 68/36; DFs individuais, notas 11). Os testes sobre a base demonstram método, não erros reais da companhia.

## 8.1 Projeto da base (Bloco 06) — aprovado pelo aluno em 23/10/2026 (D-B06-01 e D-B06-02)
"""

PARTE_E_GER = """## 8.2 Geração, conciliação e dicionário (Bloco 07)

**Arquivo entregue:** `CPFL_SINTETICA_Base_AFC_2025_registrada.csv.gz` (14.678.974 bytes; SHA-256 877d4a0256af842b859617f22c71678f30749e75b724c20cd205895ef85e4bb0), gerado por `gerar_base_cpfl_v2.py` com `config_base_cpfl_v2.json` (semente 231020069) e verificado por `verificar_base_cpfl_v2.py`.

| Distribuidora | Registros | Total (R$) | Saldo publicado (R$ mil) | Diferença |
|---|---:|---:|---:|---:|
| CPFL Paulista | 213.372 | 12.617.237.000,00 | 12.617.237 | 0,00 |
| RGE | 215.362 | 12.734.234.000,00 | 12.734.234 | 0,00 |
| CPFL Piratininga | 64.897 | 3.836.600.000,00 | 3.836.600 | 0,00 |
| CPFL Santa Cruz | 7.369 | 435.548.000,00 | 435.548 | 0,00 |
| **Total** | **501.000** | **29.623.619.000,00** | **29.623.619** | **0,00** |

Fonte: resumo do verificador (reexecutado em pasta limpa em 23/10/2026, RV12-09). Detalhe na planilha CPFL_B07_Conciliacao_Verificacoes_Base.xlsx (aba Conciliacao).

**Dicionário de dados (13 campos):**

| Campo | Tipo | Definição | Natureza |
|---|---|---|---|
| id_registro | texto | Chave primária AFC-SIM-0000001 a AFC-SIM-0501000, atribuída após embaralhamento | Sintético |
| id_bem_tecnico | texto | Identifica o bem físico; repetição = indício de duplicidade | Sintético |
| distribuidora | texto | CPFL Paulista, RGE, CPFL Piratininga, CPFL Santa Cruz | Nome real; alocação sintética |
| categoria_cadastrada | texto | Redes, transformadores, postes, medidores, subestações | Sintético |
| data_incorporacao | data | Entre 1985 e 2025, compatível com a vida útil | Sintético |
| vnr_base_simulado_rs | decimal | VNR unitário da categoria × fator aleatório; não é VNR homologado | Sintético |
| fator_atualizacao_simulado | decimal | Substituto didático do IPCA acumulado (DF25 nota 4, p. 59) | Sintético |
| fator_residual_simulado | decimal | 1 − idade/vida útil (mínimo 0,01) | Sintético, dependente |
| status_cadastral | texto | ATIVO ou BAIXADO | Sintético |
| data_baixa | data ou vazio | Vazio quando ATIVO | Sintético |
| valor_registrado_rs | decimal | Saldo em 31/12/2025, conciliado por distribuidora | Sintético; total conciliado |
| data_base | data | 2025-12-31 | Constante |
| origem_dados | texto | SINTETICO em todas as linhas | Rótulo obrigatório |

**Qualidade (16 verificações, F01–F16):** nenhuma falha de geração; 1.000 pares de `id_bem_tecnico` repetidos e 1.000 bens BAIXADO com valor são exceções do desenho, tratadas no PT 530. Reprodução em pasta limpa com hash idêntico (Bloco 07 e Bloco 12).

**Uso nos testes (Bloco 08):** ver PT 530 e PT 450. Erros inseridos, base de referência e ponte de efeitos ficaram em pasta reservada até o congelamento dos testes (19:55:53 de 23/10/2026) e estão em `CPFL_SINTETICA_Reservados_pos_congelamento.zip`.
"""

LIGACAO_RISCOS = """**7.6 Ligação entre riscos, respostas, procedimentos e resultados**

| Risco | Resposta e PTs | Modalidade | Resultado e limite |
|---|---|---|---|
| R01 Ativo financeiro da concessão (avaliação, classificação) — significativo | PG-ESTIM; PT 500, 520, 530, 540 | [Pub] analíticos, conciliações e sensibilidade; [S] base sintética; [P] base homologada e laudo | Saldos conciliados (PDF × CVM × DFs individuais); VNR 2025 +12,2% sem explicação pública (DH-02); método demonstrado na simulação |
| R02 Ativo contratual — significativo | PG-ESTIM; PT 315, 330, 540 | [Pub] saldos e PAA; [P] modelo e medições | Evidência insuficiente (PT 500) |
| R03 Receita não faturada — significativo | PG-REC; PT 330, 520 | [Pub] saldo e PAA; [P] controles de medição e recálculo | Evidência insuficiente (PT 500) |
| R16 Burla de controles — significativo | PT 240, 540 | [P] teste de lançamentos; [Pub] indicador de viés | Evidência insuficiente; viés não concluído |
| R06 Dívidas e covenants | PG-PASS; PT 505, 570 | [Pub] notas 18–19 e release; [S] minutas CF-04 | Covenant divulgado 2,30x × 3,75x, sem recálculo contratual |
| R07 Provisões e contingências | PG-PASS; PT 501, 560 | [Pub] movimentação; [S] carta jurídica não enviada | Conciliado; IRRF Jantus a verificar (DH-01) |
| R13 Partes relacionadas | PT 550, 505 | [Pub] nota 31 × BP; [P] atas e confirmações | Saldos conciliados; completude não verificada |
| R14 Consolidação | PG-CONS; PT 600 | [Pub] segmentos e CVM; [P] eliminações | Conciliações sem diferença; eliminações não testadas |
| R17 Continuidade | PT 570 | [Pub] liquidez, vencimentos e captações | Sem dúvida significativa identificada com evidência pública |
"""

PARTE_G_ANEXOS = """
| Pasta do repositório | Conteúdo | Observação |
|---|---|---|
| `01_Dossie/` | Dossie_CPFL_2025_231020069_v1.0 (PDF e DOCX) | Documento integrado com os 27 PTs, 7 programas, conclusão e minutas |
| `02_Base_sintetica/` | Base CSV.gz (501.000 registros), gerador, configuração, verificador, conciliação (xlsx), projeto B06, reservados pós-congelamento | Dados SINTÉTICOS |
| `03_Testes_amostragem/` | Pré-registro, congelamento, códigos e saídas do Bloco 08; planilha B08 | Não são fatos da companhia |
| `04_Planilhas/` | Materialidade e riscos (B04), grupo (B05), análises B09–B11, revisão B12, conferência CVM B13, dados reais B02, controles B01 | Fórmulas recalculadas, 0 erros |
| `05_Papeis/` | 27 PTs em texto (Markdown) e minutas NÃO ENVIADAS | Mesmo conteúdo do dossiê |
| `06_Controle/` | ESTADO_DO_PROJETO, DECISOES, PENDENCIAS | Rastreabilidade |
| `07_Codigo/` | Scripts de montagem do dossiê e das planilhas | Reprodução do documento |

Fontes públicas (DF, ITR, release, normas) **não são republicadas**: são identificadas no Apêndice B com documento, página e endereço de origem.
"""

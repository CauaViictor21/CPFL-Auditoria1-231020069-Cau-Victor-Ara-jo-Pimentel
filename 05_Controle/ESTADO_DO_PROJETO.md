# ESTADO DO PROJETO — Dossiê de auditoria didático CPFL Energia S.A. (2025)

UnB · Auditoria 1 (CCA0024) · Turma 02 · 2026.2 · Matrícula 231020069 · Entrega: 25/10/2026 (link GitHub)
Última atualização: 24/10/2026, Bloco 13 (montagem final) (preparação assistida por IA)

> Trabalho acadêmico. Nenhuma opinião profissional é emitida. Não houve contato com a CPFL, auditores ou terceiros.

## 1. Onde está cada coisa
- Fontes originais: Drive › `231020069---Prova-2-AUD1--main` (pastas 01–08) — preservadas.
- Insumos das etapas 1–5: Drive › `MANDAR PARA O CLAUDE PRO` (23 arquivos) — preservados (base v1 e gabaritos da etapa 1 = histórico, nunca abertos).
- Produção: `09_Elaboracao_do_trabalho_CPFL` (00_Controle, 01_Dados_reais, 02_Planejamento, 03_Base_sintetica, 04_Testes, 05_Papeis, 06_Dossie, 07_Entrega, 99_Trabalho).
- Dossiê vigente: `TRABALHO FINAL`. Versões anteriores: `06_Dossie`. Fontes, códigos e PTs em texto: zip mais recente em `99_Trabalho`.
- Base sintética v2: `03_Base_sintetica` (gerador, config, verificador, base CSV.gz, planilha de conciliação, projeto B06; reservados publicados após o congelamento).
- Testes do Bloco 08: `04_Testes`.
- Pacote final do repositório (Bloco 13): `07_Entrega` › CPFL-Auditoria1-231020069.zip (100 arquivos, README incluído).

## 2. Estado por bloco
| Bloco | Estado | Evidência de aceite |
|---|---|---|
| B01 Início, requisitos, mapa normativo | **CONCLUÍDO com pendência PB01-01 (CVM)** | Controles xlsx; relatório PDF B01 |
| B02 Entidade e saldos | **CONCLUÍDO com pendências PB01-01, PB02-02, PB02-03** | 01_Dados_reais |
| B03 EC, 200, 210, 220, 230 | **CONCLUÍDO** | Dossiê v0.1 |
| B04 240, 250, 300, 315, 320, 330 + 6 programas | **CONCLUÍDO** | 02_Planejamento; dossiê v0.2 |
| B05 402, 600 | **CONCLUÍDO** | 02_Planejamento; dossiê v0.3 |
| B06 Projeto da base | **CONCLUÍDO** (D-B06-01 e D-B06-02 aprovadas pelo aluno em 23/10/2026) | 03_Base_sintetica: CPFL_B06_Projeto_Base_Sintetica (PDF/DOCX) |
| B07 Geração, conciliação e qualidade | **CONCLUÍDO** (PT 500 iniciado) | 03_Base_sintetica: base CSV.gz (SHA 877d4a02…4bb0), gerador, verificador, CPFL_B07_Conciliacao_Verificacoes_Base.xlsx; dossiê v0.4 (43 p.) |
| B08 530 / 450 simulado | **CONCLUÍDO** (PT 530 concluído; PT 450 parcela simulada; PT 330 e PT 500 atualizados) | 04_Testes: pré-registro (19:54), congelamento (19:55:53), CPFL_B08_Amostragem_Testes_Distorcoes.xlsx, zip de código e saídas; dossiê v0.5 (49 p.) |
| B09 510, 520, 540, 550 | **CONCLUÍDO** | 02_Planejamento: CPFL_B09_Abertura_Analiticos_Estimativas_PartesRel.xlsx (0 erros); dossiê v0.6 (59 p.) |
| B10 501, 505, 560, 570 | **CONCLUÍDO** | 02_Planejamento: CPFL_B10_Litigios_Confirmacoes_Eventos_Continuidade.xlsx (0 erros) e minutas de confirmação NÃO ENVIADAS (PDF/DOCX); dossiê v0.7 (68 p.) |
| B11 260, 265, 580; fechamento 450/500 | **CONCLUÍDO** | 02_Planejamento: CPFL_B11_Comunicacoes_Distorcoes_Evidencia.xlsx (0 erros) e minutas NÃO ENVIADAS (PDF/DOCX); dossiê v0.8 (77 p.) com os 27 PTs e a conclusão integrada |
| B12 Revisão técnica | **CONCLUÍDO** (revisão automatizada, não independente) | 00_Controle: CPFL_B12_Revisao_Tecnica_Cobertura.xlsx (14 achados; matriz final: 29 de 33 obrigações atendidas, 4 pendentes do B13/aluno); dossiê v0.9 (79 p.) |
| B13 Word/PDF/GitHub | **CONCLUÍDO — repositório publicado em 24/10/2026; falta o teste em janela anônima e a postagem do link (aluno)** | Dossiê v1.0 (106 p.); pacote do repositório com README (testado em pasta limpa); conferência PDF × CVM (182 valores, 0 sem explicação) |

PTs redigidos: 27 de 27 + 6 programas por ciclo + conclusão integrada (seção 7). Nenhum procedimento futuro foi marcado como executado.

## 3. Resumo dos blocos concluídos
- **B01–B05:** ver versão 5 deste arquivo (histórico) e dossiê v0.3.
- **B06:** composição do ativo financeiro da concessão por distribuidora obtida nas notas 11 das DFs individuais (Paulista 12.617.237; RGE 12.734.234; Piratininga 3.836.600) e Santa Cruz por diferença (435.548), provada pela movimentação (435.547, ±1). DV19: base v1 usava proporções hipotéticas. Projeto v2 aprovado.
- **B07:** base v2 gerada (501.000 linhas = 500.000 bens + 1.000 duplicidades do desenho); total e 4 distribuidoras conciliados com diferença R$ 0,00; 16 testes de integridade sem falha; reprodução em pasta limpa com 4 hashes idênticos; arquivos reservados não lidos e congelados por hash; PT 500 iniciado; dossiê v0.4.

- **B08:** desenho registrado antes da execução; T1–T4 em 100% da base (4.000 registros com distorção de valor/existência; 996 de categoria); distorção conhecida líquida R$ 117.484.338,18; MUS n = 385 → UML R$ 704,3 mi > DT → ampliação n2 = 492 sem distorções → conhecida + UML residual R$ 303,19 mi ≤ DT; congelamento por hash; comparação pós-congelamento: 100% de detecção em T1–T3, 99,6% em T4 (4 omissões no piso de depreciação), 0 falsos positivos. Não é teste cego independente.

- **B09:** 61 linhas de abertura DF24 × DF25 sem diferença (sem reapresentação; rubrica de mútuo renomeada); opinião 2024 da PwC sem ressalvas (evidência indireta, DV20); analítico do VNR: +139.479 (+12,2%) > limite, concentrado na Paulista (não explicado; 2024 aderente −0,4%); conciliação nota 11 × nota 34 exata; sensibilidade: IPCA ±1 p.p. = ±66% da materialidade global, base ±2% = ±146%; renovação: reclassificação de 29.599.494 para intangível em 2026 (ITR 2T26) tratada como evento novo; partes relacionadas: mútuo SGEL 4.412.650 conciliado, completude não verificada.

- **B10:** litígios conciliados (provisões 1.740.903; possíveis 10.748.481 = 26,6x a materialidade global); IRRF Jantus (139.291) = condição existente em 31/12/2025, reconhecimento a verificar; segmentos conciliados com o LAIR; 8 minutas de confirmação NÃO ENVIADAS; linha do tempo de eventos com datas reais (relatório 04/03/2026; aditivos 06/05/2026; corte da pesquisa 23/10/2026); continuidade: CCL −1.259.649, cobertura 0,61x (release), covenant DL/EBITDA 2,30x divulgado × limite 3,75x (não verificado).

- **B11:** PT 260 (10 assuntos mapeados; minuta não enviada); PT 265 (6 condições: 1 sintética, 2 hipóteses, 1 ponto de divulgação, 1 limitação de acesso, 1 erro do preparador; nenhuma deficiência significativa real); PT 580 (minuta com 12 representações, sem data e sem assinatura); PT 450 consolidado (nenhuma distorção real; sintética líquida 117.484; hipóteses IRRF Jantus e VNR não acumuladas, 69% da global no pior caso); PT 500 fechado (matriz: R02, R03 e R16 insuficientes; R01 parcial); PT 220 com revisões RV-B03 a RV-B11; conclusão integrada sem opinião.

- **B12:** 3 erros comprovados corrigidos (modalidades fora das 3 categorias em 33 procedimentos; revisão analítica final 520-05 executada; debêntures 30.641.585 na nota 34 g, DV21); PT 560 com corte atualizado (sem fato relevante novo); vigência 240 (R2)/570 (R1) reconfirmada (FC31); 47 citações item × página sem erro; base e testes reproduzidos em pasta limpa com hashes idênticos; nenhuma afirmação indevida de execução. Três pontos para validação do aluno (aba Pontos_Validacao).

- **B13:** conferência DF25 × CVM (BP e DFC consolidados: 168 idênticos, 8 arredondamentos, 4 agregações, 2 subtotais derivados, 0 sem explicação); governança confirmada na CVM (Comitê de Auditoria e Conselho Fiscal); melhorias de forma a partir da análise de lacunas (capa, sumário, rodapé com paginação, legenda de modalidades e marcas, modelo de PT, campo requisito × orientação × julgamento nos 27 PTs, versão/estado por PT, programa PG-CONS, seção 8 com a base sintética, ligação risco-resposta-resultado, anexos digitais e minutas no dossiê); pacote do repositório montado e reprodução testada. Os 25 lotes CSV salvos pelo aluno no Drive são da base v1 (histórica, 500.000 linhas, colunas diferentes) e não substituem a base v2.

## 4. Não executado (com motivo)
- Conferência PDF × CVM da DRE consolidada: arquivo da CVM acima do limite de leitura (BP e DFC conferidos).
- Cadastro real de bens, base de remuneração da ANEEL e laudo de VNR: sem acesso (PT 500, procedimentos 500-06 e 500-07 planejados).

## 5. Cronograma
| Dia | Meta |
|---|---|
| Qui 22/10 | B01–B05 ✔ |
| Sex 23/10 | B06 ✔; B07 ✔; B08 ✔; B09 ✔; B10 ✔ |
| Sex 23/10 (noite) | B11 ✔; B12 ✔ |
| Sáb 24/10 | B13 montagem ✔; publicação no GitHub ✔ |
| Até Dom 25/10 | Teste em janela anônima e postagem do link pelo aluno |

## 6. Próximo passo
Repositório publicado: https://github.com/CauaViictor21/CPFL-Auditoria1-231020069-Cau-Victor-Ara-jo-Pimentel (100 arquivos idênticos ao pacote; base com SHA-256 conferido). Falta: o aluno testar o acesso em janela anônima e postar o link na atividade até 25/10/2026.

# -*- coding: utf-8 -*-
"""PTs do Bloco 10: PT 501, PT 505, PT 560 e PT 570."""
PREP = "Matrícula 231020069 — preparação assistida por IA (Claude), conferida contra as fontes citadas"
DATA = "23/10/2026"
PLAN = "CPFL_B10_Litigios_Confirmacoes_Eventos_Continuidade.xlsx"
MIN = "CPFL_B10_Minutas_Confirmacao_NAO_ENVIADAS (PDF/DOCX)"
PTS = []

# --------------------------------------------------------------------------- 501
PTS.append(dict(
codigo="PT 501", titulo="Evidência de auditoria — considerações específicas: estoques, litígios e informações por segmento",
norma="NBC TA 501 (NORMAS p. 471–482). Itens: 4–8 (estoques: acompanhamento da contagem, contagem em outra data, impossibilidade, estoque com terceiros; p. 474–475), 9–12 (litígios e reclamações: procedimentos para identificar, comunicação com advogados externos, recusa, representações; p. 475–476), 13 (informações por segmento; p. 476).",
objetivo="Obter evidência sobre (a) a existência e a condição dos estoques, (b) a integridade dos litígios e das reclamações e a adequação de provisões e divulgações, e (c) a apresentação das informações por segmento. A aplicabilidade de cada parte é fundamentada pela relevância.",
conta="Estoques 236.566 (BP p. 34/2); provisões para riscos 1.740.903 e depósitos judiciais 805.776 (nota 22, p. 94/62); perdas possíveis 10.748.481 (p. 95/63); segmentos (nota 30, p. 103/71).",
afirmacoes="Existência e condição (estoques); integridade, avaliação e divulgação (litígios — R07 do PT 315); apresentação (segmentos).",
populacao=f"DF25 p. 34–36, 94–96, 103; {PLAN}, abas PT501_Litigios e PT501_Estoques_Segm; {MIN} (modelo CF-08).",
procedimentos=[
 ("501-01", "Estoques: aplicabilidade, analítico 2025 × 2024 e plano de acompanhamento de contagem por amostra", "Realizado com evidência pública (analítico) / Planejado por falta de acesso (contagem)"),
 ("501-02", "Litígios: conciliar a movimentação das provisões (4 naturezas) e o quadro de perdas possíveis com o total divulgado", "Realizado com evidência pública"),
 ("501-03", "Litígios: relacionar os casos individuais divulgados e medir sua grandeza frente à materialidade", "Realizado com evidência pública"),
 ("501-04", "Carta de circularização jurídica aos advogados externos (item 10)", "Planejado por falta de acesso — modelo CF-08 NÃO ENVIADO"),
 ("501-05", "Leitura de atas, contas de honorários jurídicos e sistemas de processos (item 9)", "Planejado por falta de acesso"),
 ("501-06", "Segmentos: conciliar o LAIR dos segmentos com a DRE (item 13)", "Realizado com evidência pública"),
],
corpo="""
**1. Estoques (itens 4–8): aplicabilidade limitada**

- Saldo de 236.566 (0,29% do ativo; +6,8% sobre 2024).
- Isoladamente, fica abaixo da materialidade global (58%) e da de execução (78%). Mesmo assim, é relevante o bastante para não ser ignorado.
- O item 4 exige acompanhar a contagem **se o estoque for relevante**. O programa PG-EST (Bloco 04) prevê extensão reduzida: acompanhamento de contagem em almoxarifados selecionados por valor e testes de obsolescência de materiais de manutenção.
- **Não houve presença em inventário.** O procedimento é apenas planejado.

**2. Litígios e reclamações (itens 9–12)**

| Teste | Resultado |
|---|---|
| Movimentação das provisões: 1.561.980 + 423.111 − 107.475 − 335.067 + 198.354 = 1.740.903 | Confere (±1 de arredondamento por natureza) |
| Perdas possíveis: soma das 5 naturezas = 10.748.481 (2024: 10.182.096) | Confere; aumento de 566.385 |
| Perdas possíveis ÷ materialidade global | **26,6 vezes**: não provisionado, mas sensível à mudança de prognóstico |

**Casos individuais relevantes (p. 94–96):**

- CEEE Prev 519.456 (possível)
- ABRAGEL 380.500 (possível)
- Jataí: 51.712 possível, 927.018 remoto
- IRPJ/CSLL ERSA/SMITA 504.722 (possível)
- Ágio RGE 650.519
- **IRRF Jantus:** decisão definitiva desfavorável em novembro de 2025; débito de 139.291 em 31/12/2025, quitado em janeiro de 2026 por 60.950 com benefícios da Lei 14.689/2023.
- **Ativo contingente** da CPFL Brasil contra a ANEEL (cálculo da AGU de 4.678.104), corretamente não reconhecido. Está em negociação de acordo; o ganho não é praticamente certo.

**Ponto de auditoria (Jantus):** com a decisão definitiva antes de 31/12/2025, havia **obrigação presente** na data do balanço. As DF não mostram de forma explícita em qual rubrica o débito foi reconhecido. Verificação planejada no PT 560. O valor fica abaixo da execução (46%), mas acima do trivial: acumular no PT 450 se não estiver reconhecido.

**Procedimentos indisponíveis:**

- carta aos advogados externos (modelo CF-08, **não enviado**);
- leitura de atas e de contas de honorários;
- indagação ao jurídico interno;
- representações formais (item 12; PT 580).

**3. Segmentos (item 13)**

A soma do LAIR dos seis segmentos (8.091.246) é igual ao LAIR consolidado, com diferença zero. A distribuição responde por 65,9% e concentra o ativo financeiro da concessão. A conciliação foi feita no B05 (DV18).
""",
evidencias=f"DF25 p. 34–36, 94–96, 103; {PLAN}; {MIN}. Referências cruzadas: PT 315 (R07), PT 450, PT 505, PT 560, PT 580, PT 600 (segmentos), programa PG-EST.",
resultados="Provisões e perdas possíveis conciliadas com o divulgado. Perdas possíveis equivalem a 26,6 vezes a materialidade global. Obrigação do IRRF Jantus em 31/12/2025 a verificar quanto ao reconhecimento. Segmentos conciliados. Estoques sem procedimento físico.",
conclusao="Os números divulgados de litígios e segmentos são internamente consistentes. A integridade dos litígios e a adequação dos prognósticos dependem da carta jurídica e das indagações, planejadas. Não é conclusão sobre a CPFL.",
limitacoes="Sem contagem física, sem advogados, sem atas. Prognósticos e valores são da administração.",
))

# --------------------------------------------------------------------------- 505
PTS.append(dict(
codigo="PT 505", titulo="Confirmações externas — desenho, controle e minutas (MODELOS NÃO ENVIADOS)",
norma="NBC TA 505 (NORMAS p. 483–496). Itens: 6 (definições: confirmação positiva, negativa, não resposta, exceção), 7 (controle do auditor sobre as solicitações; p. 489), 8–9 (recusa da administração), 10–11 (confiabilidade das respostas), 12 (não resposta: procedimentos alternativos), 13 (resposta positiva indispensável), 14 (exceções), 15 (confirmação negativa: condições), 16 (avaliação; p. 490–491). Apoio: NBC TA 500 A5 e NBC TA 330 item 19.",
objetivo="Desenhar os procedimentos de confirmação externa que seriam aplicados e preparar minutas e um controle de circularização. Nada foi enviado.",
conta="Caixa + TVM 2.905.082; mútuo SGEL 4.412.650; debêntures detidas pela SGBP 325.563; empréstimos e debêntures 29.055.727; derivativos 595.863; recebíveis 6.377.562; provisões jurídicas 1.740.903 (BP p. 34–35; notas 18, 19, 22, 31).",
afirmacoes="Existência e direitos (caixa, recebíveis); integridade e obrigações (dívidas, partes relacionadas); avaliação (derivativos); integridade (litígios).",
populacao=f"{PLAN}, aba PT505_Controle (CF-01 a CF-08); {MIN}.",
procedimentos=[
 ("505-01", "Definir saldos, partes confirmantes (categorias institucionais), tipo de confirmação e critério de seleção", "Realizado com evidência pública (desenho documental)"),
 ("505-02", "Preparar minutas CF-01 a CF-08 e o controle de circularização", "Simulado para fins didáticos — MODELOS NÃO ENVIADOS"),
 ("505-03", "Enviar, acompanhar, avaliar respostas, investigar exceções e aplicar procedimentos alternativos", "Planejado por falta de acesso"),
],
corpo="""
**1. O que foi feito e o que não foi**

- Foram preparados oito modelos (CF-01 a CF-08) e um controle com valores do BP, critério de seleção e procedimento alternativo para não resposta.
- **Nenhum foi enviado.**
- Não há destinatário pessoal, resposta, exceção ou confirmação recebida.
- As colunas de envio e resposta do controle estão vazias de propósito.

**2. Escolhas de desenho (julgamento didático)**

| Saldo | Tipo | Por quê |
|---|---|---|
| Partes relacionadas: mútuo SGEL e debêntures da SGBP | Positiva com saldo, 100% | Risco R13; transação significativa (PT 550) |
| Bancos | Positiva em branco | Reduz o viés de concordância; inclui garantias, derivativos e restrições |
| Dívidas e derivativos | Positiva por contraparte | Integridade de obrigações; *covenants* e *waivers* (PT 570) |
| Recebíveis | Positiva (maiores) e negativa (pulverizados) | A negativa só é admitida nas condições do item 15 |
| Litígios (carta jurídica) | Carta aos advogados | NBC TA 501 item 10 |

**3. Controle do auditor (item 7)**

- O auditor define a informação e a parte confirmante.
- O endereço é verificado de forma independente.
- O envio é feito pelo auditor, e a resposta vai direto a ele.
- Respostas por e-mail exigem verificação da origem (itens 10–11).
- **Recusa da administração** (itens 8–9): avaliar as razões, reavaliar o risco de fraude (PT 240) e comunicar à governança se não for razoável.
- **Não resposta** (item 12): procedimentos alternativos do controle, como extratos, pagamentos subsequentes e documentos de B3 e CCEE.
- **Resposta positiva indispensável** (item 13): sem ela, não há alternativa. É o caso do mútuo SGEL, pela natureza do risco.
""",
evidencias=f"{PLAN} (PT505_Controle); {MIN}; DF25 notas 18, 19, 22, 31, 34. Referências cruzadas: PT 330, PT 501, PT 550, PT 570.",
resultados="Oito modelos e controle de circularização preparados. Nenhum enviado. Nenhuma resposta.",
conclusao="O desenho atende aos requisitos de controle da NBC TA 505. Não há evidência externa obtida: os saldos permanecem suportados apenas pelas DF auditadas e pelos demais PTs.",
limitacoes="Proibição do trabalho de contatar terceiros. Destinatários apenas por categoria. Valores ilustrativos extraídos das DF.",
))

# --------------------------------------------------------------------------- 560
PTS.append(dict(
codigo="PT 560", titulo="Eventos subsequentes",
norma="NBC TA 560 (R1) (NORMAS p. 625–638). Itens: 5 (definições: data das DF, data de aprovação, data do relatório, data de divulgação), 6–7 (procedimentos entre a data das DF e a do relatório; p. 628), 8 (ajuste ou divulgação), 9 (representação formal; p. 629), 10–13 (fatos conhecidos após o relatório e antes da divulgação), 14–17 (fatos conhecidos após a divulgação; p. 630–631). Estrutura contábil: CPC 24 (eventos que originam ajuste × que não originam).",
objetivo="Identificar eventos entre 31/12/2025 e a data do relatório (04/03/2026) que exijam ajuste ou divulgação. Separar o que foi conhecido depois, com datas reais, sem tratar informação de 2026 como conhecida em 31/12/2025.",
conta="DF consolidadas de 2025 como um todo; destaque para o ativo financeiro da concessão (renovação), dívidas (captações), litígios (IRRF) e partes relacionadas (mútuos SGEL).",
afirmacoes="Integridade, avaliação e divulgação. Ligação com R01, R07, R13, R17 e R18.",
populacao=f"DF25 notas 2.1 (p. 45), 22 (p. 96), 37 (p. 113–114) e relatório (p. 32); ITR 1T26 (p. 42, 55, 58); ITR 2T26 (p. 43–44, 49, 59–60, 65); Fato Relevante de 08/05/2026; Release 4T25; RI CPFL (lista de comunicados de 2026) e notícias, consultados em 23/10/2026; {PLAN}, aba PT560_Linha_Tempo.",
procedimentos=[
 ("560-01", "Registrar as datas-marco: DF 31/12/2025; autorização 23/02/2026; CA e relatório 04/03/2026; publicação 20/03/2026", "Realizado com evidência pública"),
 ("560-02", "Ler a nota 37 e as notas com fatos de 2026 e classificar ajuste × divulgação (itens 6–8)", "Realizado com evidência pública"),
 ("560-03", "Ler os ITRs de 1T26 e 2T26 e os comunicados de 2026 e posicioná-los na janela correta (itens 10–17)", "Realizado com evidência pública"),
 ("560-04", "Pesquisa pública de fatos posteriores ao ITR 2T26 (corte efetivo em 23/10/2026)", "Realizado com evidência pública"),
 ("560-05", "Indagar a administração e a governança, ler as atas pós-31/12 e obter representação formal (itens 7(b)–(c) e 9)", "Planejado por falta de acesso"),
 ("560-06", "Verificar o reconhecimento do débito do IRRF Jantus em 31/12/2025", "Planejado por falta de acesso"),
],
corpo="""
**1. Datas-marco (item 5)**

| Marco | Data | Fonte |
|---|---|---|
| Data das demonstrações | 31/12/2025 | DF25 |
| Autorização da emissão pela administração | 23/02/2026 | Nota 2.1, p. 45 |
| Aprovação pelo Conselho e **data do relatório do auditor** (PwC, sem modificação) | 04/03/2026 | Nota 2.1, p. 45; relatório, p. 32 |
| Publicação legal | 20/03/2026 | Publicidade legal (URL na ata metodológica da base) |
| **Corte efetivo da pesquisa deste trabalho** | **23/10/2026** | Pesquisa web e RI realizada nesta data |

**2. Janela 1 — da data das DF ao relatório (itens 6–9): fatos refletidos na DF25**

| Evento | Classificação (CPC 24) | Tratamento na DF25 | Avaliação |
|---|---|---|---|
| IRRF Jantus: decisão definitiva em nov/2025; débito de 139.291; quitado em jan/2026 por 60.950 | **Condição existente em 31/12** (obrigação presente) → ajuste | Descrito na nota 22 (p. 96/64) e na nota 10 (p. 68) | Verificar se o passivo estava reconhecido (560-06). Se não estiver, distorção abaixo da execução, a acumular no PT 450 |
| Debêntures de jan/2026 (Paulista 1.700.000; Santa Cruz 100.000; Transmissão 100.000) | Condição posterior → divulgação | Nota 37.3, p. 114/82 | Adequado |
| Incorporação da CPFL Geração pela CPFL Brasil (AGE de 02/02/2026) | Condição posterior; sem efeito no consolidado | Nota 37.1 | Adequado |
| Curtailment (Lei 15.269/2025) | Ativo contingente incerto | Nota 37.2: nada reconhecido | Adequado em princípio (ganho não praticamente certo) |
| Renovação: aprovações da ANEEL em 2025; decisão do MME pendente | Incerteza existente em 31/12 | Nota 1.3, p. 44/12 | Divulgado sem quantificação (PT 540) |

**3. Janela 2 — após a publicação (itens 14–17): fatos de 2026 que não eram conhecidos em 31/12/2025 nem em 04/03/2026**

- **06/04/2026:** despacho do MME.
- **06/05/2026:** assinatura dos aditivos e prorrogação por 30 anos (ITR 1T26 nota 23.3, p. 55/22).
- **No ITR do 2T26:** reclassificação prospectiva de 29.599.494 do ativo financeiro da concessão para o intangível (nota 11, p. 49/15).
- **Mútuos com a SGEL:** 200.000 (abril) e 1.805.000 (julho), divulgados em comunicados de transação com partes relacionadas de 27/04 e 07/07/2026.
- **Tarifas:** RTA da Paulista e RTP da Santa Cruz (abril/2026).
- **Outros:** temporal em Ribeirão Preto (julho/2026) e regulamentação do curtailment (Portaria MME 140/2026).

**Avaliação.** São condições **surgidas depois** da data do relatório. A NBC TA 560 não obriga o auditor a executar procedimentos após a divulgação (item 14). Só haveria ação se surgisse fato que, **conhecido na data do relatório**, poderia ter levado a alterá-lo. Nenhum dos fatos acima se enquadra nisso: a assinatura dos aditivos é evento novo, tratado prospectivamente pela própria companhia em 2026. Esses fatos não são tratados como conhecidos em 31/12/2025.

**4. Corte da pesquisa (23/10/2026)**

- **Fontes consultadas em 23/10/2026:**
  - lista de comunicados ao mercado de 2026 no RI da CPFL. Último: alteração do calendário de eventos em 14/10/2026, com a conferência do 3T26 remarcada de 13/11 para 16/11/2026;
  - aviso de dividendos de 02/10/2026;
  - notícias sobre o pagamento de dividendos em 23/10/2026.
- **Resultado:** nenhum fato relevante novo após o ITR 2T26 (autorizado em 10/08/2026) foi identificado.
- **Limitação:** o conteúdo dos comunicados de partes relacionadas de 27/04 e 07/07/2026 não pôde ser aberto pelo link do RI, que retornou outro documento. Ele foi inferido das notas dos ITRs (23.2 e 24.1).
- A data de corte deve ser **atualizada e efetivamente pesquisada** na revisão final (Bloco 12).
""",
evidencias=f"DF25 p. 32, 44–45, 68, 96, 113–114; ITR 1T26 p. 42, 55, 58; ITR 2T26 p. 43–44, 49, 59–60, 65; Fato Relevante de 08/05/2026; RI CPFL (comunicados de 2026, consultados em 23/10/2026); {PLAN} (PT560_Linha_Tempo). Referências cruzadas: PT 450, PT 501, PT 540, PT 550, PT 570, PT 580.",
resultados="Quatro eventos da janela 1 avaliados (um de ajuste a verificar: IRRF Jantus; três de divulgação adequada) e a incerteza da renovação divulgada. Onze eventos de 2026 posicionados após a divulgação, sem efeito sobre as DF de 2025. Corte efetivo da pesquisa em 23/10/2026.",
conclusao="Com evidência pública, os eventos subsequentes conhecidos até 04/03/2026 estão divulgados. Fica pendente a confirmação do reconhecimento do IRRF Jantus. Fatos de 2026 não alteram as DF de 2025.",
limitacoes="Sem indagações, atas e representação formal. Dois comunicados de 2026 não puderam ser lidos na íntegra. Publicação legal em 20/03/2026 obtida de fonte secundária (URL citada na ata da base).",
))

# --------------------------------------------------------------------------- 570
PTS.append(dict(
codigo="PT 570", titulo="Continuidade operacional",
norma="NBC TA 570 (versão de 2016, aplicável a 2025; a (R1) de 2026 só se aplica a partir de 2027 — D-B01-02; NORMAS p. 639–659). Itens: 10–11 (avaliação de risco e atenção contínua; p. 642–643), 12–14 (revisão da avaliação da administração; **13: período de pelo menos 12 meses a partir da data das DF**; p. 643), 15 (período posterior), 16 (procedimentos adicionais: planos, previsão de caixa, fatos novos, representações), 17–19 (conclusão: incerteza relevante; p. 644), 20–24 (relatório; p. 645), 25 (comunicação).",
objetivo="Avaliar se há eventos ou condições que possam levantar dúvida significativa sobre a continuidade, considerando liquidez, dívida, vencimentos, compromissos, cláusulas restritivas e eventos adversos no horizonte de 12 meses a partir de 31/12/2025, e se as divulgações são adequadas.",
conta="Capital circulante líquido −1.259.649 (nota 1.4, p. 44/12); passivos financeiros não descontados de 48.423.044 (nota 34 g, p. 113/81); dívida bruta de 29.055.727; compromissos de 79.413.507 (nota 36, p. 113/81); covenants (notas 18–19, p. 82–83).",
afirmacoes="Apresentação e divulgação (base de continuidade). Risco R17 (baixo) do PT 315.",
populacao=f"DF25 p. 34–39, 44, 82–83, 110–114; Release 4T25 p. 3–4 e 15; ITRs de 2026; {PLAN}, aba PT570_Liquidez.",
procedimentos=[
 ("570-01", "Indicadores de liquidez e endividamento; vencimentos em 12 meses (nota 34 g) e cobertura", "Realizado com evidência pública"),
 ("570-02", "Covenants: parâmetros divulgados × indicador divulgado pela administração (release); folga e cenários", "Realizado com evidência pública (informação da administração, não auditada)"),
 ("570-03", "Fatores atenuantes: geração de caixa, captações de jan/2026, refinanciamentos, perfil de prazo, controlador", "Realizado com evidência pública"),
 ("570-04", "Obter e testar a avaliação da administração e a previsão de caixa de 12 meses (itens 12–16)", "Planejado por falta de acesso"),
 ("570-05", "Recalcular os covenants com as definições contratuais e confirmar ausência de waivers (CF-04)", "Planejado por falta de acesso"),
 ("570-06", "Representação formal sobre os planos e a continuidade (item 16(e); PT 580)", "Planejado por falta de acesso"),
],
corpo="""
**1. Horizonte e versão aplicável**

- A versão de 2016 exige que a avaliação cubra **pelo menos 12 meses a partir da data das DF** (item 13): até 31/12/2026.
- A NBC TA 570 (R1), publicada em 2026, não se aplica a 2025.

**2. Eventos e condições (item 10)**

| Indicador | Valor | Leitura |
|---|---|---|
| Capital circulante líquido | (1.259.649); 2024: (818.989) | Condição a avaliar; a companhia informa plano de financiamento aprovado (nota 1.4) |
| Liquidez corrente | 0,93 | Abaixo de 1 |
| Passivos financeiros em até 12 meses (fluxo não descontado) | 12.916.273 | Soma das três primeiras faixas da nota 34 g |
| Caixa + TVM | 2.905.082 | Cobertura de amortizações de 12 meses de 0,61x segundo a companhia (release p. 15) |
| Caixa operacional de 2025 | 7.162.797 | Fator atenuante |
| Dividendos de 2025 a pagar em 2026 | 4.300.000 (proposta; AGO de 29/04/2026) | Saída relevante, pagos em parcelas até out/2026 |
| Captações de jan/2026 | 1.900.000 (debêntures, nota 37.3) | Fator atenuante |
| Compromissos de compra de energia e obras | 79.413.507, dos quais 24.987.753 em até 1 ano | Repassáveis em grande parte pela tarifa (distribuição) |

A cobertura simples, (caixa + FCO − dividendos + captações) ÷ saídas de 12 meses, é **0,59x** (cenário didático). Ela **ignora** capex e refinanciamentos, e por isso **não** indica, sozinha, incapacidade de pagamento.

**3. Cláusulas restritivas (sem concluir pelo cumprimento)**

- **Parâmetros:** dívida líquida/EBITDA ajustado ≤ 3,75; EBITDA ajustado/resultado financeiro ≥ 2,25; PL/(PL + dívida líquida) ≥ 0,28 (consolidado). Para as distribuidoras, dívida líquida/EBITDA ≤ 4,00 (notas 18–19, p. 82–83).
- **Posição divulgada:** a administração informa **2,30x** de dívida líquida/EBITDA no critério dos covenants (release 4T25, p. 4 e 15), com dívida líquida de 30.530 e EBITDA pró-forma de 13.280 milhões. Recálculo aritmético: 2,30.
- **Folga calculada:** o EBITDA poderia cair 38,7%, ou a dívida líquida subir 19.270 milhões, antes de atingir 3,75 (cenário didático).
- **Limites da evidência:**
  - o EBITDA "ajustado/pró-forma" usa consolidação proporcional e inclui o mútuo da SGEL, definições contratuais não públicas;
  - os dois outros índices não estão divulgados;
  - o indicador com dados auditados (dívida bruta − caixa − TVM) ÷ (resultado do serviço + D&A) = 1,98 é **diferente** do covenant e serve apenas de referência;
  - a afirmação da administração de que não houve não conformidade (p. 83) **não foi verificada**.
- **Não se conclui pelo cumprimento** dos covenants (570-05, planejado).

**4. Fatores atenuantes e eventos de 2026**

- **Atenuantes:**
  - geração de caixa recorrente;
  - perfil de dívida de 4,13 anos (release p. 15);
  - acesso a mercado: debêntures de jan/2026 e empréstimos de jul–ago/2026 (ITR 2T26 nota 24.2);
  - mútuos do controlador (SGEL) em 2026;
  - prorrogação das concessões das três maiores distribuidoras por 30 anos (assinada em 06/05/2026).
- **Eventos adversos identificados:** temporal de Ribeirão Preto (julho/2026; baixas e provisões divulgadas no ITR 2T26, nota 24.4) e curtailment na geração. Nenhum aponta para dúvida significativa.
- **Dependência de refinanciamento:** a cobertura de 0,61x indica refinanciamento contínuo, o que é característico do setor. Seria testada com a previsão de caixa da administração (item 16(c)).

**5. Diferenciação das fontes**

| Origem | Exemplos |
|---|---|
| Avaliação da administração | Nota 1.4 e afirmações das notas 18–19. **Não obtida em detalhe** |
| Informação pública auditada | BP, DFC e notas 34 e 36 |
| Informação pública não auditada | Release (2,30x; 0,61x) |
| Cenário didático | Coberturas e folgas calculadas |

O relatório da PwC não traz seção de incerteza relevante sobre continuidade (DF25 p. 26–32). Isso **não** é usado como conclusão deste trabalho.
""",
evidencias=f"DF25 p. 26–32, 34–39, 44, 82–83, 110–114; Release 4T25 p. 3–4 e 15; ITR 1T26 e 2T26 (notas de eventos subsequentes); {PLAN} (PT570_Liquidez); {MIN} (CF-04). Referências cruzadas: PT 315 (R17), PT 520, PT 560, PT 580.",
resultados="CCL negativo e cobertura de 12 meses inferior a 1 com caixa próprio, mitigados por geração de caixa, acesso a captações e covenant divulgado em 2,30x contra o limite de 3,75x. Cumprimento de covenants não verificado.",
conclusao="Com a evidência pública disponível, não foram identificados eventos ou condições que, somados, indiquem dúvida significativa. A conclusão sobre a existência ou não de incerteza relevante exige a avaliação da administração, a previsão de caixa e o recálculo contratual dos covenants, todos planejados. Não é opinião sobre a CPFL.",
limitacoes="Sem previsão de caixa, contratos ou definições de EBITDA. Indicadores do release não auditados. Ratings não lidos (arquivos incompletos no Drive, PB01-04).",
))

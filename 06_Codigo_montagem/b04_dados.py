# -*- coding: utf-8 -*-
"""Dados do Bloco 04 (riscos, respostas, programas, fraude, leis, cronograma).
Compartilhado entre a planilha (b04_planejamento.py) e os PTs (pts_b04.py).
Fontes: DF25 = DF25 CPFL.pdf (pág. física/impressa). Saldos em R$ mil, consolidado 31/12/2025."""

MG, ME, TRIV = 404562.30, 303421.725, 20228.115   # PT 320 (fórmulas na planilha)

# Fatores de risco inerente (NBC TA 315 R2, item 12(f)): C=complexidade, S=subjetividade, M=mudança, I=incerteza, V=suscetibilidade a viés/fraude
# Campos: id, conta/processo, saldo, fonte, afirmações, risco, fatores, prob(1-3), mag(1-3), nível, significativo, fundamento da significância
RISCOS = [
 ("R01","Ativo financeiro da concessão (nota 11)",29623619,"DF25 p. 34/2; p. 68/36; PAA 3 p. 29","Avaliação; classificação; apresentação","Mensuração a VNR e bifurcação (ativo financeiro × contratual × intangível) incorretas","C,S,I,V",3,3,"Alto","Sim","Estimativa com alta incerteza; PAA 3; 36,5% do ativo; ajuste VNR de 1.285.173 = 15,9% do LAIR"),
 ("R02","Ativo contratual (transmissão e distribuição)",12859523,"DF25 p. 34/2; nota 15 p. 76; PAA 1 p. 27","Avaliação; exatidão","Taxa de desconto, margens e RAP distorcem ativo e receita de remuneração","C,S,I",3,3,"Alto","Sim","Estimativa de longo prazo; PAA 1"),
 ("R03","Receita não faturada",1763858,"DF25 p. 28 (PAA 2); nota 3.11 p. 54","Ocorrência; corte; exatidão","Estimativa baseada em carga, faturamento e perdas técnicas/comerciais; depende de TI","C,S,I,V",3,3,"Alto","Sim","PAA 2; dados de sistemas; presunção de fraude em receita (240 item 27)"),
 ("R04","Receita operacional líquida (demais componentes)",44367780,"DF25 p. 36/4; nota 26 p. 100–101","Ocorrência; corte; exatidão; classificação","Componentes regulados (tarifa, CDE R$ 3.103.700, construção R$ 5.879.424) registrados incorretamente","C,M,V",2,3,"Moderado","Não (ver R03)","Receita tarifária homologada pela ANEEL reduz discricionariedade; risco de fraude concentrado em R03 e comercialização"),
 ("R05","Consumidores, concessionárias e permissionárias",6377562,"DF25 p. 34/2; nota 7 p. 61","Existência; avaliação (PDD)","Perdas esperadas insuficientes; PDD de 361.253 em 2025","S,I",2,3,"Moderado","Não","Estimativa com histórico e regras regulatórias"),
 ("R06","Empréstimos, financiamentos e debêntures",29055727,"DF25 p. 35/3; notas 18–19 p. 79–85","Integridade; exatidão; classificação CP/LP; divulgação","Classificação e encargos incorretos; covenants (cross default) — administração declara cumprimento","C,M",2,3,"Moderado","Não","Liquidação antecipada de 5.616.000 em debêntures e captações de 10.266.269 em 2025 (p. 39, 85)"),
 ("R07","Provisões fiscais, cíveis, trabalhistas e regulatórias",1740903,"DF25 p. 35/3; nota 22 p. 94–96","Integridade; avaliação; divulgação","Classificação provável/possível e mensuração subavaliadas","S,I,V",2,3,"Moderado","Não","Julgamento jurídico"),
 ("R08","Derivativos (ativos 595.863; passivos 403.394)",595863,"DF25 p. 34–35; nota 34 p. 108","Avaliação; apresentação","Valor justo e hedge contábil incorretos","C,S",2,2,"Moderado","Não","Correção da matriz preliminar: 999.257 somava ativos e passivos (DV17)"),
 ("R09","Ativos e passivos financeiros setoriais",2402307,"DF25 p. 34/2; nota 9 p. 64","Avaliação; classificação","Componentes tarifários e prazos de recuperação incorretos","C,M,I",2,3,"Moderado","Não","Dependem de atos ANEEL (ex.: REH 3.452/2025, nota 26.2)"),
 ("R10","Imobilizado e intangível",16268718,"DF25 p. 34/2; notas 14 e 16 p. 75–78","Existência; avaliação; classificação","Capitalização indevida; vidas úteis; amortização do intangível da concessão (332.792)","S",2,2,"Moderado","Não","Sem provisão de recuperação em 2025 (nota 14)"),
 ("R11","Caixa e equivalentes",2229320,"DF25 p. 34/2; nota 5 p. 60","Existência; direitos","Saldos inexistentes ou restritos","—",1,2,"Baixo","Não","Alta verificabilidade externa"),
 ("R12","Estoques",236566,"DF25 p. 34/2","Existência; avaliação","Quantidades e obsolescência","—",1,1,"Baixo","Não","0,3% do ativo; 58% da materialidade global — abaixo dela isoladamente"),
 ("R13","Partes relacionadas e mútuos (passivo)",4412650,"DF25 p. 35/3; nota 31 p. 103","Integridade; divulgação","Transações com o controlador (State Grid) não identificadas ou divulgadas","V",2,3,"Moderado","Não","Mútuos passivos subiram de 2.485.694 para 4.393.234 (LP)"),
 ("R14","Consolidação do grupo",81099930,"DF25 nota 1 p. 41–42; nota 13 p. 69","Integridade; apresentação","Eliminações e componentes incorretos; julgamento de controle conjunto da Chapecoense (51%, acordo de acionistas — nota 13.9.3, p. 74)","C",2,3,"Moderado","Não","Grupo com 4 distribuidoras, geração, transmissão e comercialização"),
 ("R15","TI — medição, faturamento e interfaces","—","DF25 p. 28 (PwC usou especialistas de TI)","Integridade; exatidão; corte","Dados de origem e interfaces incorretos","C",2,3,"Moderado","Não","Afeta R03; controles não testados"),
 ("R16","Burla de controles pela administração","—","NBC TA 240 item 32","Todas","Lançamentos manuais, estimativas enviesadas, transações incomuns","V",2,3,"Alto","Sim","Risco significativo por exigência da NBC TA 240 (item 28 e item 32)"),
 ("R17","Continuidade e liquidez",None,"DF25 p. 34–35; p. 39/7","Divulgação","Liquidez corrente 0,93; serviço da dívida","I",1,3,"Baixo","Não","Caixa operacional 7.162.797; LL 5.742.552; covenants cumpridos segundo a administração (p. 83, 85)"),
 ("R18","Renovação das concessões (premissa do ativo financeiro)",None,"Fato Relevante 08/05/2026; fatos relevantes de 28/03/2025 citados","Avaliação; divulgação","Premissa de indenização ao fim da concessão afetada pela prorrogação de 30 anos","S,M,I",2,3,"Moderado","Não (vinculado a R01)","Processo iniciado em 2025; aditivos assinados em 2026 — analisar no PT 540/560"),
 ("R19","PIS/COFINS sobre ICMS — créditos e devolução a consumidores",None,"DF25 p. 34–35; nota 8 p. 62–63","Avaliação; classificação; divulgação","Ativo 4.096.542 e passivo 3.402.844 mal mensurados ou classificados","C,M",2,3,"Moderado","Não","Saldos relevantes ligados a decisões judiciais (STF tema 69)"),
]

# Respostas (NBC TA 330): id risco -> lista (procedimento, natureza, época, extensão, modalidade, PT)
RESPOSTAS = {
 "R01":[("Reexecutar a movimentação da nota 11 e conciliar com BP, DRE (ajuste VNR na receita) e DFC","Substantivo — recálculo","Final","100% da movimentação","Realizado com evidência pública (B02: CC05/CC06)","500"),
        ("Testar existência e valor de bens na base de remuneração por amostragem (MUS)","Substantivo — detalhe","Final","Amostra estatística sobre população de 500.000 registros","Simulado para fins didáticos","530"),
        ("Avaliar método, premissas (VNR, índices) e viés; sensibilidade","Substantivo — estimativa","Final","Premissas-chave","Realizado com evidência pública + simulação","540"),
        ("Inspecionar laudos de avaliação e base de remuneração homologada pela ANEEL","Substantivo — inspeção","Final","Distribuidoras relevantes","Planejado por falta de acesso","540")],
 "R02":[("Ler contratos de concessão e RAP; recalcular remuneração com dados públicos","Substantivo","Final","Lote principal","Planejado (contratos parcialmente no Drive)","540"),
        ("Analítico: receita de remuneração/ativo contratual médio","Analítico substantivo","Final","Por segmento","Realizado com evidência pública","520")],
 "R03":[("Recalcular receita não faturada (carga cativa × tarifas por classe)","Substantivo — recálculo","Final","Por distribuidora","Planejado por falta de acesso","540"),
        ("Comparar faturamento de janeiro/2026 com estimativa de dezembro/2025 (corte)","Substantivo — eventos subsequentes","Após fechamento","Total","Planejado por falta de acesso","560"),
        ("Testar controles de TI (ITGC) de medição e faturamento","Teste de controles","Interina","Sistemas-chave","Planejado por falta de acesso","330/402")],
 "R04":[("Analítico de receita por componente (tarifa, CDE, construção, VNR) 2025 × 2024","Analítico substantivo","Final","Componentes da nota 26","Realizado com evidência pública","520"),
        ("Conciliar receita de construção com adições de ativo contratual (DFC 4.963.868)","Substantivo","Final","Total","Realizado com evidência pública","520")],
 "R05":[("Circularização de grandes clientes livres (modelo)","Confirmação externa","Final","Seleção por valor","Simulado/Planejado (modelo não enviado)","505"),
        ("Recálculo de PDD e análise de aging","Substantivo","Final","Por distribuidora","Planejado por falta de acesso","540")],
 "R06":[("Conciliar movimentação de dívida com DFC (captação 10.266.269; amortização 10.727.722)","Substantivo","Final","Total","Realizado com evidência pública","500/570"),
        ("Recalcular índices de covenants com dados públicos, nas definições divulgadas","Substantivo","Final","Índices consolidados","Realizado com evidência pública (limitado às definições disponíveis)","570"),
        ("Confirmação de saldos com bancos e agentes fiduciários (modelo)","Confirmação externa","Final","Principais contratos","Simulado/Planejado (não enviado)","505")],
 "R07":[("Ler nota 22; analítico da movimentação; cartas de advogados (modelo)","Substantivo","Final","Processos relevantes","Realizado com evidência pública + modelo não enviado","501/505")],
 "R08":[("Conciliar derivativos com nota 34 e recalcular valor justo indicativo","Substantivo","Final","Principais contratos","Planejado por falta de acesso (curvas e contratos)","540")],
 "R09":[("Analítico da movimentação dos ativos/passivos setoriais × atos ANEEL","Analítico substantivo","Final","Por distribuidora","Realizado com evidência pública (parcial)","520")],
 "R10":[("Analítico de depreciação/amortização (DFC 2.397.217) sobre saldo médio","Analítico substantivo","Final","Total","Realizado com evidência pública","520"),
        ("Inspeção física e de documentos de adições","Substantivo","Final","Amostra","Planejado por falta de acesso","501")],
 "R11":[("Confirmação bancária (modelo) e conciliações","Confirmação externa","Final","Todas as contas relevantes","Simulado/Planejado (não enviado)","505"),
        ("Conferir caixa DFC × BP","Substantivo","Final","Total","Realizado com evidência pública (B02: CC03)","500")],
 "R12":[("Análise de aplicabilidade; inventário apenas se justificado","Analítico","Final","Total","Realizado com evidência pública (análise)","501")],
 "R13":[("Mapear partes relacionadas (nota 31) e testar completude por fontes externas","Substantivo","Final","Todas as partes divulgadas","Realizado com evidência pública (parcial; FR truncado)","550")],
 "R14":[("Mapear componentes e avaliar materialidade de componentes; testar eliminações","Substantivo","Final","Componentes significativos","Realizado com evidência pública + planejado","600")],
 "R15":[("Entendimento de TI (NBC TA 315 item 25–26) e controles complementares de prestadores","Avaliação de risco","Interina","Fluxos de receita","Planejado por falta de acesso","315/402")],
 "R16":[("Teste de lançamentos contábeis (240 item 33(a)): critérios de seleção","Substantivo","Final","Lançamentos manuais e de fechamento","Planejado por falta de acesso; critérios aplicados na base sintética","240/530"),
        ("Revisão retrospectiva de estimativas (240 item 33(b))","Substantivo","Final","VNR, não faturada, PDD, provisões","Realizado com evidência pública (comparação 2024→2025)","240/540"),
        ("Avaliar razão de negócio de transações significativas incomuns (240 item 33(c))","Substantivo","Final","Mútuos com controlador; liquidação antecipada de debêntures","Realizado com evidência pública (parcial)","240/550")],
 "R17":[("Análise de liquidez, vencimentos e covenants","Analítico","Final","Consolidado","Realizado com evidência pública","570")],
 "R18":[("Avaliar efeito da renovação nas premissas do ativo financeiro e classificação ajuste × divulgação","Substantivo — estimativa / eventos subsequentes","Final","Distribuidoras renovadas","Realizado com evidência pública","540/560")],
 "R19":[("Ler nota 8; conciliar ativo e passivo de PIS/COFINS; analisar compensações","Substantivo","Final","Saldos consolidados","Realizado com evidência pública (parcial)","500/520")],
}

PROGRAMAS = [
 ("PG-REC","Receitas","R03, R04, R15, R16","44.367.780 (DRE p. 36/4)","Aplicável — maior classe de transações; presunção de fraude",
  ["Analítico por componente da nota 26 (expectativa: variação tarifária + mercado) [Pub] — PT 520",
   "Conciliar receita de construção × adições de ativo contratual e intangível [Pub] — PT 520",
   "Recalcular receita não faturada e testar corte com faturamento subsequente [P] — PT 540/560",
   "Testar ITGC de medição/faturamento e controles de interface [P] — PT 330/402",
   "Teste de lançamentos contábeis em contas de receita (critérios: manuais, fim de período, valores redondos) [P] — PT 240"]),
 ("PG-DISP","Disponibilidades","R11","2.229.320 + TVM 675.762 (BP p. 34/2)","Aplicável — saldo acima da materialidade global; risco baixo",
  ["Conferir caixa da DFC × BP [Pub — feito no B02, CC03] — PT 500",
   "Confirmação bancária: modelo e controle de circularização (não enviado) [S/P] — PT 505",
   "Conciliações bancárias e extratos de janeiro/2026 [P] — PT 505",
   "Verificar restrições e garantias (cauções, nota 12) [Pub] — PT 500"]),
 ("PG-EST","Estoques","R12","236.566 (BP p. 34/2)","Aplicabilidade limitada — 58% da materialidade global; 0,3% do ativo",
  ["Analítico de variação 2025 × 2024 (+6,8%) [Pub] — PT 520",
   "Análise qualitativa: materiais de manutenção da distribuição; ausência de PAA [Pub] — PT 501",
   "Acompanhamento de inventário apenas se o risco aumentar (NBC TA 501 item 4) [P] — PT 501"]),
 ("PG-IMOB","Imobilizado (e intangível/ativos da concessão)","R10, R01, R02","9.375.879 + intangível 6.892.839 (BP p. 34/2)","Aplicável — distinguir imobilizado societário da infraestrutura da concessão (ICPC 01)",
  ["Movimentação das notas 14 e 16 e conciliação com DFC (aquisições 369.941) [Pub] — PT 500",
   "Analítico de depreciação/amortização sobre saldo médio [Pub] — PT 520",
   "Avaliar indicadores de redução ao valor recuperável (nenhuma provisão em 2025) [Pub] — PT 540",
   "Inspeção física e de documentos de adições [P] — PT 501",
   "Base sintética: testes de existência/valor no ativo financeiro da concessão [S] — PT 530"]),
 ("PG-PASS","Passivos","R06, R07, R13, R17, R19","Passivo total 57.595.420 (BP p. 35/3)","Aplicável — dívida de 29.055.727 e provisões de 1.740.903",
  ["Movimentação de empréstimos e debêntures × DFC [Pub] — PT 500",
   "Recalcular covenants nas definições divulgadas (notas 18–19) [Pub, limitado] — PT 570",
   "Busca de passivos não registrados: pagamentos subsequentes (ITR 1T26) [Pub, parcial] — PT 560",
   "Cartas a advogados e confirmações de credores (modelos não enviados) [S/P] — PT 505/501",
   "Fornecedores: analítico de prazo médio [Pub] — PT 520"]),
 ("PG-ESTIM","Estimativas","R01, R02, R03, R05, R07, R08, R18","AFC 29.623.619; ativo contratual 12.859.523; não faturada 1.763.858","Aplicável — três PAA são estimativas",
  ["Selecionar estimativa principal: VNR do ativo financeiro da concessão [Pub] — PT 540",
   "Sensibilidade reproduzível das premissas (índice de atualização, taxa) [S/Pub] — PT 540",
   "Revisão retrospectiva 2024 → 2025 (240 item 33(b)) [Pub] — PT 240/540",
   "Avaliar efeito da renovação das concessões (Fato Relevante 08/05/2026) [Pub] — PT 540/560",
   "Avaliar indicadores de viés da administração [Pub] — PT 540"]),
]

FRAUDE = [
 ("Incentivo/pressão","Remuneração e metas vinculadas a lucro e EBITDA; covenants financeiros (cross default)","Notas 18–19 p. 82–85 (covenants); FR item 8 indisponível (truncado)","Inferência"),
 ("Incentivo/pressão","Dividendos relevantes ao controlador (dividendos pagos 3.519.769 em 2025)","DF25 p. 39/7","Fato"),
 ("Oportunidade","Estimativas complexas com alta subjetividade (VNR, receita não faturada, ativo contratual)","PAA 1–3, DF25 p. 27–29","Fato"),
 ("Oportunidade","Transações com o controlador (mútuos de 4.412.650)","DF25 p. 35/3; nota 31","Fato"),
 ("Oportunidade","Grupo complexo, com controladas em conjunto e reorganizações (incorporação da CPFL Geração em 2026)","Nota 1 p. 41–42; nota 37.1 p. 113","Fato"),
 ("Atitude/racionalização","Sem indícios públicos identificados; não testável sem acesso (entrevistas)","—","Não avaliável"),
 ("Fator mitigador (não elimina o risco)","Comitê de Auditoria e Conselho Fiscal com regimentos publicados; Novo Mercado; auditoria por firma de grande porte","Drive pasta 03 (regimentos 2025/2026); FR 2025 item 1.1","Fato"),
]

LEIS = [
 ("Efeito direto","Lei 6.404/76 e Resoluções CVM (estrutura contábil; CPC aprovados pela CVM)","DF25 nota 2.1 p. 45","Elaboração e divulgação","Ler DF e conferir aderência de divulgações-chave [Pub]"),
 ("Efeito direto","Regulação tarifária ANEEL (PRORET, REH de reajuste)","Nota 26.1–26.2 p. 100–101","Receita, ativos/passivos setoriais","Conferir REH citadas e efeitos (nota 26.2) [Pub]"),
 ("Efeito direto","Contratos de concessão e Decreto 12.068/2024 (renovação)","Nota 1 p. 41; Fato Relevante 08/05/2026","Ativo financeiro da concessão","Ler aditivos e cláusulas de indenização [P/Pub]"),
 ("Efeito direto","Legislação tributária (IRPJ/CSLL, PIS/COFINS; tema 69 do STF — exclusão do ICMS)","Nota 8 p. 62–63; nota 10","Tributos, créditos e passivos com consumidores","Analítico e leitura de notas [Pub]"),
 ("Efeito direto","CDE e subsídios tarifários (Lei 12.783/2013; Lei 14.300/2022)","Nota 26.3–26.4 p. 101","Receita e contas a receber da CDE","Conciliar receita CDE 3.103.700 [Pub]"),
 ("Outras com efeito relevante","Lei 15.269/2025 (compensação por curtailment)","Nota 37.2 p. 113","Ativo contingente não reconhecido","Avaliar divulgação [Pub]"),
 ("Outras com efeito relevante","Lei Anticorrupção 12.846/2013 (política anticorrupção publicada)","Drive pasta 03 (Política Anticorrupção)","Contingências; reputação","Indagação à administração e governança [P]"),
 ("Outras com efeito relevante","Legislação ambiental (provisões de desmobilização 175.276; incêndio — perda possível de 51.712)","BP p. 35/3; nota 22 p. 95","Provisões e contingências","Leitura de nota 22; cartas a advogados [Pub/P]"),
 ("Outras com efeito relevante","Normas setoriais de qualidade (ONS/ANEEL — indicadores e penalidades)","Bases ONS/CCEE (pasta 05; não validadas)","Multas e compensações a consumidores","Validar fonte antes de uso; indicador não prova infração [P]"),
]

CRONOGRAMA = [
 ("Planejamento (estratégia, riscos, materialidade)","22/10/2026","B03–B04","PT EC–230, 240, 250, 300, 315, 320, 330"),
 ("Grupo e prestadores","23/10/2026","B05","PT 402, 600"),
 ("Base sintética e testes","23/10/2026","B06–B08","PT 500, 530, 450"),
 ("Abertura, analíticos, estimativas, partes relacionadas","24/10/2026","B09","PT 510, 520, 540, 550"),
 ("Itens específicos, confirmações, eventos, continuidade","24/10/2026","B10","PT 501, 505, 560, 570"),
 ("Comunicações e conclusão","25/10/2026","B11","PT 260, 265, 580; fechamento 450/500"),
 ("Revisão e entrega","25/10/2026","B12–B13","Revisão transversal; Word/PDF; GitHub"),
]

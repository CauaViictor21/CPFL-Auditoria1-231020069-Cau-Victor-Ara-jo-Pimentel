# Bloco 08 — Desenho dos testes, registrado ANTES da execução

CPFL Energia S.A. · Ativo financeiro da concessão (base SINTÉTICA v2) · Matrícula 231020069 · 23/10/2026

Este documento foi gravado no Drive (pasta 04_Testes) **antes** da execução dos testes. Os hashes abaixo travam o código e os parâmetros. Os arquivos reservados (referência, registro de erros e ponte) continuam fechados. A mesma IA que desenhou os erros desenhou os testes, portanto este **não** é um teste cego independente.

## 1. Objetivo, afirmações e população

| Item | Definição |
|---|---|
| Objetivo | Obter evidência (simulada) de que o saldo registrado do ativo financeiro da concessão não contém distorção relevante |
| Afirmações | Existência e direitos (duplicidades, baixas); avaliação (valor do bem); classificação (categoria) — risco significativo R01 |
| População | Base registrada: 501.000 registros; R$ 29.623.619.000,00; SHA-256 877d4a02…4bb0 |
| Completude da população | Conciliada com o BP e com as 4 distribuidoras no Bloco 07 (diferença R$ 0,00) |
| Tipo de teste | **Testes de detalhes** (substantivos). Não há testes de controles: os controles não foram testados por falta de acesso |

## 2. Procedimentos integrais (100% da população, por computador)

Estes procedimentos **não são amostragem** (NBC TA 530 item 5: amostragem é aplicar o procedimento a menos de 100% dos itens).

| Teste | Regra fixada antes da execução | Afirmação |
|---|---|---|
| T1 | Repetição de `id_bem_tecnico`. O registro de `id_registro` maior em cada par é tratado como excedente (convenção) | Existência |
| T2 | `status_cadastral` = BAIXADO com valor > 0: distorção = valor integral | Existência / direitos |
| T3 | Recalcular VNR × fator × residual × k_d, sendo k_d a mediana de valor ÷ (VNR × fator × residual) na distribuidora. Exceção se o desvio for maior que 1% | Avaliação |
| T4 | Residual esperado = máx(0,01; 1 − idade/vida útil da categoria **cadastrada**). Exceção se a diferença for maior que 0,00015 | Classificação |

O limite de 1% do T3 cobre o arredondamento do fator residual a 4 casas, que gera erro relativo de até 0,5% nos bens mais depreciados (residual de 0,01). O limite do T4 cobre o arredondamento a 4 casas.

## 3. Amostragem estatística por unidade monetária (MUS)

| Elemento | Definição | Natureza |
|---|---|---|
| Finalidade | Representa o procedimento que, na auditoria real, não se faz por computador: inspeção de documentos e do laudo, verificação física. Na simulação, o "valor auditado" de cada item sorteado vem da aplicação de T1–T3 ao próprio item | Simulado |
| Unidade amostral | Cada real (R$ 1) do saldo registrado; o item que contém a unidade sorteada é testado | Exigência (530 item 5; A2) |
| Seleção | Sistemática por intervalo monetário, com ponto inicial aleatório (semente 2310200698) sobre os valores acumulados na ordem de `id_registro` | Aleatória: atributo (a) de amostragem estatística |
| Avaliação | Projeção por *taint* × intervalo e limite superior de distorção pelo método de Stringer (fatores de Poisson a 95%) | Teoria das probabilidades: atributo (b) |
| Distorção tolerável (DT) | R$ 303.421.730,00 = materialidade de execução | Julgamento (530 A3; D-B04-01) |
| Risco de aceitação incorreta | 5% (fator de confiança 2,9957 para zero erros) | Julgamento: risco significativo, sem confiança em controles |
| Distorção esperada (DE) | R$ 45.513.259,50 (15% da DT) | Julgamento didático |
| Fator de expansão | 1,6 | Literatura (AICPA, *Audit Sampling*), não norma |
| Tamanho | n = VC × FC ÷ (DT − DE × FE) = 29.623.619.000 × 2,9957 ÷ (303.421.730 − 72.821.215) = **385** | Cálculo |
| Intervalo | J = 29.623.619.000 ÷ 385 ≈ R$ 76.944.465 | Cálculo |
| Itens de seleção integral | Itens ≥ J são testados integralmente e excluídos da projeção. O maior item da base tem cerca de R$ 3,6 milhões, então não se espera nenhum | Regra |
| Saldos nulos ou negativos | Não participam do MUS. O código para se existirem (o Bloco 07 mostrou que não há) | Regra |
| Item selecionado mais de uma vez | Testado uma vez; a seleção é contada uma vez por ponto de seleção | Regra |
| Subavaliação | O MUS é pouco eficaz para subavaliação; ela é coberta pelo T3 (100%) | Limitação conhecida |

Regra de decisão: se o limite superior de distorção (UML) for menor ou igual à DT, a amostra apoia, com 95% de confiança, a conclusão de que a superavaliação não excede a DT. Caso contrário, os procedimentos devem ser ampliados.

## 4. Protocolo de congelamento

1. Registrar este documento no Drive.
2. Executar `testes_b08.py`, que lê apenas a base registrada e `parametros_b08.json`.
3. Gravar os hashes de código, parâmetros e saídas em `B08_congelamento.json` e registrá-lo no Drive.
4. **Só então** regenerar e abrir a ponte e o registro de erros reservados, para medir detecções, omissões e falsos positivos.

## 5. Hashes travados

| Arquivo | SHA-256 |
|---|---|
| parametros_b08.json | 72df419dbf2b66fef3948b83ac443afbf237f681c562fea71424f5922d9bc0df |
| testes_b08.py | 74af872f9599ce61651f4e0735415e5bb18bfe2e070d978d7914166b87d504b2 |
| Base registrada | 877d4a0256af842b859617f22c71678f30749e75b724c20cd205895ef85e4bb0 |

Normas: NBC TA 530, itens 5–15 e A3, A10–A13, A18–A23 (NORMAS p. 533–540); NBC TA 450, itens 5, 6 e 11 (p. 429–430); NBC TA 500, item 10 (p. 449); NBC TA 330 (p. 379).

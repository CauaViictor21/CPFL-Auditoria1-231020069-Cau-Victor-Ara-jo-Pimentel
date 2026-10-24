# Dossiê de auditoria — CPFL Energia S.A. (demonstrações de 2025)

**Universidade de Brasília · Auditoria 1 (CCA0024) · Turma 02 · 2026.2 · Matrícula 231020069**
Trabalho individual. Versão final **1.0**, de 24/10/2026.

> **Aviso.** Este é um exercício acadêmico. Não é auditoria independente, não emite opinião profissional e não fornece nenhuma forma de asseguração sobre a CPFL Energia S.A.
>
> - Usa apenas documentos públicos (CVM, B3, RI da companhia) e uma base de dados **SINTÉTICA**, criada para fins didáticos.
> - Ninguém foi contatado: nem a companhia, nem seus auditores, clientes ou fornecedores.
> - Todas as confirmações, comunicações e cartas são **minutas NÃO ENVIADAS** e não estão assinadas.
> - O trabalho foi preparado com assistência de IA (Claude). Nenhuma revisão humana independente foi simulada.

## 1. Por onde começar

1. Abra `01_Dossie/Dossie_CPFL_2025_231020069_v1.0.pdf`. É o documento integrado, com 106 páginas:
   - os 27 papéis de trabalho;
   - os 6 programas por ciclo e o programa de consolidação;
   - a conclusão integrada;
   - a base sintética;
   - fontes, divergências e minutas.
2. A versão editável é o `.docx`, com o mesmo conteúdo.
3. A seção 4 do dossiê traz o índice dos papéis. A planilha `03_Planilhas/CPFL_B12_Revisao_Tecnica_Cobertura.xlsx` traz a matriz de cobertura das 33 obrigações do enunciado e o registro de revisão.

## 2. Organização do repositório

| Pasta | Conteúdo |
|---|---|
| `01_Dossie/` | Dossiê final em PDF e DOCX |
| `02_Base_e_testes/base_v2/` | **Base sintética** (`saida/CPFL_SINTETICA_Base_AFC_2025_registrada.csv.gz`), gerador, configuração, verificador e arquivos reservados (erros inseridos), publicados só após o congelamento dos testes |
| `02_Base_e_testes/testes_b08/` | Pré-registro e congelamento do desenho, códigos dos testes (T1–T4, MUS) e saídas |
| `02_Base_e_testes/*.xlsx, *.pdf` | Projeto da base (B06), conciliação e verificações (B07), amostragem e distorções (B08) |
| `03_Planilhas/` | Planilhas editáveis: controles, dados reais, materialidade e riscos, grupo, análises, revisão técnica e conferência PDF × CVM. `dados_cvm/` traz os extratos da CVM usados nessa conferência |
| `04_Papeis_e_minutas/` | Os 27 PTs em texto (Markdown) e as minutas NÃO ENVIADAS (PDF) |
| `05_Controle/` | Estado do projeto, decisões e pendências |
| `06_Codigo_montagem/` | Scripts usados para montar o dossiê e as planilhas. Eles têm caminhos do ambiente de preparação e servem só para rastreabilidade |

## 3. Base sintética (exigência do enunciado)

| Item | Valor |
|---|---|
| Conta | Ativo financeiro da concessão (consolidado): R$ 29.623.619 mil, 36,5% do ativo total (DF25 p. 34/2) |
| Arquivo | `02_Base_e_testes/base_v2/saida/CPFL_SINTETICA_Base_AFC_2025_registrada.csv.gz` (CSV compactado, UTF-8, separador vírgula) |
| Registros | **501.000**: 500.000 bens + 1.000 duplicidades previstas no desenho |
| Tamanho | 14.678.974 bytes |
| SHA-256 | `877d4a0256af842b859617f22c71678f30749e75b724c20cd205895ef85e4bb0` |
| Conciliação | Total e quatro distribuidoras iguais aos saldos publicados, com diferença de R$ 0,00 |
| Dicionário | Dossiê, seção 8.2; planilha B07, aba `Dicionario` |

Todos os registros têm `origem_dados = SINTETICO`. Os registros **não** são dados internos da CPFL.

## 4. Como reproduzir

Requisitos: Python 3.10 ou superior. Para o MUS, também é preciso o `scipy`:

```
pip install scipy
```

Execute sempre numa **cópia** da pasta, para preservar os originais.

```
cd 02_Base_e_testes/base_v2
python gerar_base_cpfl_v2.py          # regenera a base em saida/ (semente 231020069)
python verificar_base_cpfl_v2.py      # 16 verificações e conciliação por distribuidora
```

O SHA-256 da base regenerada deve ser igual ao da tabela acima. Isso foi testado em pasta limpa em 23 e 24/10/2026.

```
cd ../testes_b08
python testes_b08.py                  # T1–T4 em 100% da base e amostra MUS (n = 385)
python avaliacao_complementar_b08.py  # ampliação do MUS na população residual (n2 = 492)
```

Os arquivos CSV de `saida_b08/` saem idênticos aos entregues. Nos arquivos JSON, só mudam os campos de data e hora da execução.

Para a comparação com os erros inseridos:

1. descompacte `base_v2/CPFL_SINTETICA_Reservados_pos_congelamento.zip` dentro de `base_v2/`;
2. rode `python comparar_gabarito_b08.py` sobre as saídas **entregues**.

O script confere os hashes congelados antes de comparar. Por isso, ele recusa saídas regeneradas, que têm data e hora novas.

## 5. Independência dos testes (limitação declarada)

O desenho dos testes foi registrado no Drive antes da execução, às 19:54 de 23/10/2026, e congelado por hash às 19:55:53. Os arquivos reservados só foram abertos depois disso.

A mesma IA desenhou os erros e os testes. Por isso, os resultados **não** são apresentados como teste cego independente (PT 530).

## 6. Fontes

As fontes públicas (DF 2025 e 2024, ITR de 2026, release, Formulário de Referência e normas do CFC) **não são republicadas** aqui. Elas estão listadas no Apêndice B do dossiê, com documento, página, endereço e data de acesso.

Os dados da CVM vêm do portal de dados abertos (DFP 2025, versão 1, documento 155108). Os extratos foram filtrados pelo CNPJ da companhia.

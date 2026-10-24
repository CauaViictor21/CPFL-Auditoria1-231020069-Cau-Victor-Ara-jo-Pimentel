# -*- coding: utf-8 -*-
"""Bloco 12: atualizações de PTs decorrentes da revisão técnica (sem PTs novos)."""
DATA = "23/10/2026"
PLAN = "CPFL_B12_Revisao_Tecnica_Cobertura.xlsx"
PTS = []

ADD_520 = """
**6. Revisão analítica final das DF (item 6) — executada no Bloco 12 (23/10/2026)**

Objetivo: verificar se as DF, como um todo, são consistentes com o entendimento da entidade obtido nos PTs. Dados: BP e DRE consolidados (DF25 p. 34–36/2–4), aba PT520_Revisao_Final da planilha B12, com fórmulas.

| Indicador | 2025 | 2024 | Variação | Consistente com o entendimento? |
|---|---:|---:|---:|---|
| Receita operacional líquida | 44.367.780 | 42.628.210 | +4,1% | Sim: reajustes tarifários (nota 26) |
| Margem bruta | 31,8% | 31,8% | 0,0 p.p. | Sim: custo de energia repassado pela tarifa |
| Resultado do serviço ÷ receita | 24,3% | 24,6% | −0,3 p.p. | Sim |
| Despesas financeiras | 4.942.969 | 4.343.203 | +13,8% | Sim: dívida estável; taxa CDI/SELIC de 14,90% no fim de 2025 (nota 34 e.2, p. 111) |
| LAIR | 8.091.246 | 8.088.893 | +0,0% | Sim |
| Taxa efetiva (IR + CS ÷ LAIR) | 29,0% | 28,8% | +0,3 p.p. | Sim |
| Ativo financeiro da concessão | 29.623.619 | 25.209.768 | +17,5% | Parcial: VNR acima da expectativa (seção 4; PB09-01) |
| Ativo contratual (circulante + não circulante) | 12.859.523 | 11.138.706 | +15,4% | Sim: investimentos; transferência para o AFC (nota 11) |
| Ativo financeiro setorial | 2.402.307 | 730.965 | +228,6% | Explicado qualitativamente (nota 9, p. 64–65: CVA e transferência de 1.844.610 de PIS/COFINS); posição líquida setorial de 411.659 confere com a nota 34 e.2 (p. 111). Movimentação numérica não reconferida |
| PIS/COFINS a devolver (passivo) | 3.402.844 | 4.936.756 | −31,1% | Sim: transferência para o setorial (nota 9) |
| Empréstimos + debêntures | 29.055.727 | 28.788.338 | +0,9% | Sim |
| Mútuo com partes relacionadas | 4.412.650 | 2.485.694 | +77,5% | Sim: troca dos mútuos SGBP por SGEL (PT 550) |
| Caixa + TVM | 2.905.082 | 3.547.055 | −18,1% | Plausível: dividendos e amortizações (DFC p. 39); não decomposto |

**Conclusão da revisão final.** Nenhuma variação nova e inesperada além das já tratadas: o VNR (PT 540) e o ativo setorial, cuja explicação é qualitativa. Pelo item 7, o setorial ficaria para indagação, com movimentação da nota 9 a reconferir se o acesso existisse. Não altera a avaliação de riscos (PT 315).
"""

ADD_560 = """
**5. Atualização do corte em 23/10/2026, às 21h (Bloco 12)**

A lista de comunicados de 2026 do RI da CPFL foi relida integralmente no Bloco 12. Itens não citados na versão anterior:

| Data | Documento (título no RI) | Classificação | Efeito |
|---|---|---|---|
| 23/01 e 02/02/2026 | Fatos relevantes de reorganização societária | Já tratado (nota 37.1: incorporação da CPFL Geração) | Nenhum |
| 06/03/2026 | Fato relevante: renúncia de membro do Conselho de Administração (substituto eleito) | Após o relatório; governança | Nenhum nas DF de 2025 |
| 10–17/03/2026 | 21ª emissão de debêntures da CPFL Energia e 8ª da CPFL Santa Cruz | Captação após o relatório | Atenua o risco de liquidez (PT 570) |
| 01–10/09/2026 | Escritura e anúncio de início da 19ª emissão de debêntures | Captação após o relatório | Idem |
| Abr–out/2026 | Avisos de dividendos (29/04, 11/05, 01/06, 05/08, 04/09, 02/10) | Pagamento da proposta de 2025 | Saída já considerada no PT 570 |
| 15/10/2026 | Atas da 585ª e da 586ª RCA | Não lidas (conteúdo não aberto) | Desconhecido: limitação |

- **Nenhum fato relevante** foi publicado após 08/05/2026 até o corte. A conferência do 3T26 está prevista para 16/11/2026, depois da entrega.
- **Conclusão inalterada:** nenhum fato altera riscos, continuidade ou a conclusão. As novas captações reforçam o acesso a mercado já considerado no PT 570.
- **Limitação:** os valores das emissões de 2026 e o conteúdo das atas de 15/10/2026 não foram lidos. Os títulos vêm da lista do RI ([ri.cpfl.com.br](https://ri.cpfl.com.br/list.aspx?ano=2026&idCanal=cq54IMbPPtNE4sURyBMZIQ%3D%3D), acesso em 23/10/2026). A renúncia foi confirmada em notícia de 09/03/2026 (Cenário Energia). Nomes de pessoas foram omitidos.
"""

UPDATES = {
 "PT 520": dict(corpo_add=ADD_520,
   resultados_add=" Revisão analítica final (item 6, Bloco 12): sem variação nova inesperada; ativo setorial (+228,6%) explicado qualitativamente pela nota 9.",
   evidencias_add=f" Bloco 12: {PLAN} (PT520_Revisao_Final); DF25 p. 64–65 e 111."),
 "PT 560": dict(corpo_add=ADD_560,
   resultados_add=" Corte atualizado em 23/10/2026 (Bloco 12): sem fato relevante novo; novas emissões de debêntures e atas de 15/10/2026 (não lidas) registradas.",
   evidencias_add=" Bloco 12: lista de comunicados 2026 do RI (relida em 23/10/2026); Cenário Energia, 09/03/2026."),
}

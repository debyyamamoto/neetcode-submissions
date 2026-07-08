class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        menor_preco_ate_agora = prices[0]
        lucro_maximo = 0
        for preco_hoje in prices:
            lucro = preco_hoje - menor_preco_ate_agora 
            lucro_maximo = max(lucro_maximo, lucro)
            menor_preco_ate_agora = min(menor_preco_ate_agora, preco_hoje)
        if lucro_maximo >= 0:
            return lucro_maximo
        else:
            return 0
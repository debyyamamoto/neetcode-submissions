class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array_ordenado = sorted(nums)
        resposta = set()
        k = 0
        for i in range(len(nums)-1):
            ponteiro_ref = i
            k=0
            ponteiro_esquerda = ponteiro_ref+1
            ponteiro_direita = len(nums) -1 
            while ponteiro_esquerda < ponteiro_direita:
                target = -array_ordenado[ponteiro_ref]
                if array_ordenado[ponteiro_esquerda] + array_ordenado[ponteiro_direita] == target:
                    resposta.add((array_ordenado[ponteiro_ref], array_ordenado[ponteiro_direita], array_ordenado[ponteiro_esquerda]))
                soma_atual = array_ordenado[ponteiro_direita] + array_ordenado[ponteiro_esquerda]
                if(soma_atual < target):
                    ponteiro_esquerda += 1
                else:
                    ponteiro_direita -= 1
                k += 1
                
        return [list(trinca) for trinca in resposta]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ponteiro_esquerda = 0
        ponteiro_direita = len(numbers) - 1
        k = 0
        #   ^            ^
        # [-5,-3,0,2,4,6,8]
        while k != len(numbers):
            # -5 + 8 = 3
            if numbers[ponteiro_direita] + numbers[ponteiro_esquerda] == target:
                return [ponteiro_esquerda+1, ponteiro_direita+1]
            else: 
                if abs((numbers[ponteiro_esquerda+1] + numbers[ponteiro_direita])- target) < abs((numbers[ponteiro_esquerda] + numbers[ponteiro_direita-1]) - target):
                    ponteiro_esquerda += 1
                else:
                    ponteiro_direita -=1
            k += 1
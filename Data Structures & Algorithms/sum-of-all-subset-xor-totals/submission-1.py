class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i:int, soma_acumulada:int):
            if i == len(nums):
                return soma_acumulada
            
            sem = dfs(i+1, soma_acumulada)
            com = dfs(i+1, soma_acumulada ^ nums[i])

            return sem + com
        return dfs(0,0)
class Solution:
    def climbStairs(self, n: int) -> int:
        df = [-1] * (n+1)
        def dfs(soma):
            if soma == n:
                return 1
            if soma == n-1:
                return 1
            if df[soma] != -1:
                return df[soma]
            df[soma] = dfs(soma+1) + dfs(soma+2)
        
            return df[soma]
            
        return dfs(0)
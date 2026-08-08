class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        cs = []

        def dfs(i):
            if i >= len(candidates):
                if sum(cs) == target:
                    res.add(tuple(cs))
                return
            cs.append(candidates[i])
            if sum(cs) <= target:    
                dfs(i+1)
            cs.pop()
            dfs(i+1)

        dfs(0)
        ans = []
        for i in res:
            sub = []
            for w in i:
                sub.append(w)
            ans.append(sub.copy())
        
        return ans
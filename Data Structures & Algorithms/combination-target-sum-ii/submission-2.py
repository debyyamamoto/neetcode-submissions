class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cs = []
        candidates.sort()
        def dfs(i, soma_t):
            if soma_t == target:
                res.append(cs.copy())
                return 
            for j in range(i, len(candidates)):
                if soma_t + candidates[j] > target:
                    break
                if candidates[j-1] == candidates[j] and j > i:
                    continue
                cs.append(candidates[j])
                dfs(j+1, soma_t + candidates[j])
                cs.pop()

        dfs(0,0)
        return res
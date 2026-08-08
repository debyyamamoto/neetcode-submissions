class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cs = []
        candidates.sort()
        def dfs(i, soma_t):
            if soma_t == target:
                res.append(cs.copy())
                return 
            if(i==len(candidates)):
                return
            
            #i e a primeira ocorrencia
            limite = i
            while(limite < len(candidates) and candidates[limite]==candidates[i]):
                limite+=1
            
            #v[limite]==v[i] ?
            #i é a primeira ocorrencia do numero 5
            #quantos numeros 5 usar?
            #5 [i, limite)
            
            dfs(limite, soma_t)
            for j in range(i, limite):
                if soma_t > target:
                    break
                cs.append(candidates[j])
                soma_t+=candidates[j]
                dfs(limite, soma_t)
            
            while(len(cs) and cs[-1]==candidates[i]):
                cs.pop()

        dfs(0,0)
        return res
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
            quantidade = limite-i
            # [1, quantidade]
            for j in range(1, quantidade+1):
                if soma_t > target:
                    break
                cs.append(candidates[i])
                soma_t+=candidates[i]
                dfs(limite, soma_t)
            
            while(len(cs) and cs[-1]==candidates[i]):
                cs.pop()

        dfs(0,0)
        return res
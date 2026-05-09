class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencia = {}
        res = []
        final = []
        for i in nums:
            if frequencia.get(i) == None:
                frequencia[i] = 1
            else:
                l = frequencia.get(i)
                l += 1
                frequencia[i] = l

        for i, j in frequencia.items():
            heapq.heappush(res, (j, i))
            if len(res) > k:
                heapq.heappop(res)
                
        for _, j in res:
            final.append(j)    
        
        return final
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencia = {}
        res = []
        for i in nums:
            if frequencia.get(i) == None:
                frequencia[i] = 1
            else:
                l = frequencia.get(i)
                l += 1
                frequencia[i] = l
        
        final = sorted(frequencia.items(), key=lambda item: item[1])[-k:]
        for i, j in final:
            res.append(i)
        return res
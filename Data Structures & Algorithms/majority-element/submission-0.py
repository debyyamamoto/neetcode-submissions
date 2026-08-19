class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        control = {}
        for i in nums:
            control[i] = control.get(i, 0) + 1
        max = -math.inf 
        chave = 0 
        for c, i in control.items():
            if max < i:
                max = i
                chave = c
        
        return chave
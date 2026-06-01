class Solution:
    #              L R  
    # nums = [-1,0,2,4,6,8]
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) #6
        while(r > l):
            m = (r+l)//2 
            if(nums[m] == target):
                return m
            if(nums[m] < target):
                l = m + 1
            else:
                r = m
        return -1
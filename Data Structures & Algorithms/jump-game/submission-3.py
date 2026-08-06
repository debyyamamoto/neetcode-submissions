class Solution:
    def canJump(self, nums: List[int]) -> bool:
        alcance_max = 0
        
        for i in range(len(nums)):
            if i > alcance_max:
                return False

            if i + nums[i] > alcance_max:
                alcance_max = i + nums[i]

            if alcance_max > len(nums) - 1:
                return True

        return True
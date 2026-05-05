class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target
        # nums[i] == target - nums[j]
        guarda = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in guarda:
                return[guarda[complemento], i]
            guarda[num] = i
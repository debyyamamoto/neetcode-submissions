class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target
        # nums[i] == target - nums[j]
        dict = {}
        count = 0
        for i in nums:
            dict[nums[count]] = count
            count += 1
        count = 0
        for i in nums:
            if(dict.get(target - nums[count])) and count != dict[target - nums[count]]:
                return [count, dict[target - nums[count]]]
            count += 1
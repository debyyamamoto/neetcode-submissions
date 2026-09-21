class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, uns, dois = 0, 0, 0
        for e in nums:
            if e == 0:
                zeros = zeros + 1
            elif e == 1:
                uns = uns + 1
            else:
                dois = dois + 1

        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
                continue
            elif uns != 0:
                nums[i] = 1
                uns -= 1 
                continue
            else:
                nums[i] = 2
                dois -= 1 
                continue
        return nums  
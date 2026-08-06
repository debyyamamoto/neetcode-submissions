class Solution:
    def jump(self, nums: List[int]) -> int:
        pulos = 0
        alcance_max = 0
        fim_pulo_atual = 0

        for i in range(len(nums)):
            if len(nums) == 1:
                return 0
            if i + nums[i] >= alcance_max:
                    alcance_max = i + nums[i]
            if i == fim_pulo_atual and i != len(nums)-1:
                    pulos += 1
                    fim_pulo_atual = alcance_max

        return pulos 
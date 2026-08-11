
class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1
        a = 1
        b = 1
        for _ in range(2, n):
            aa = a
            bb  = b
            a = b
            b = aa+bb
            
        return b
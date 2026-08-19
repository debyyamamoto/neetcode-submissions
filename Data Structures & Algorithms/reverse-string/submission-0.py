class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            c, f = s[l], s[r]

            s[l] = f 
            s[r] = c

            r -= 1
            l += 1
        return s        
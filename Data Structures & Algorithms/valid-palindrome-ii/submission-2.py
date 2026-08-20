class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        def ehpalindromo(p):
            l = 0
            r = len(p) - 1

            while l < r:
                if p[l] == p[r]:
                    r -= 1
                    l += 1
                else:
                    return False
            return True
        for i in range(len(s)):
            resto = s[:i] + s[i+1:]
            if ehpalindromo(resto):
                return True

        return False
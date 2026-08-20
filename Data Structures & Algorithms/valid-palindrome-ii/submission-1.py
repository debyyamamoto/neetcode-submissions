class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            resto = s[:i] + s[i+1:]
            if resto == resto[::-1]:
                return True
        return False
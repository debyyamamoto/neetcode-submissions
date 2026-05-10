class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_sem_espacos = []
        for i in s:
            if not i.isalnum(): 
                continue
            else:
                s_sem_espacos.append(i.lower())
        s_sem_espacos = "".join(s_sem_espacos)
        l = 0
        r = len(s_sem_espacos) - 1
        while l < r:
            if s_sem_espacos[l] != s_sem_espacos[r]:
                return False
            l += 1
            r -= 1
        return True     
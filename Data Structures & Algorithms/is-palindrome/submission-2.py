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
        for i in range(len(s_sem_espacos)//2):
            if(s_sem_espacos[i]!=s_sem_espacos[len(s_sem_espacos)-i-1]):
                return False
        return True 
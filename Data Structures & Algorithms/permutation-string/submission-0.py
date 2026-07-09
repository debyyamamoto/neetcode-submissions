class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        frequencia_s2 = {}
        frequencia_s1 = {}
        if len(s1) > len(s2):
            return False
        # eu quero saber se em alguma janela eu tenho uma permutação dos termos da primeira string
        # frequencia dos caracteres da string 1

        for i in s1:
            frequencia_s1[i] = frequencia_s1.get(i, 0) + 1
        for r in range(len(s2)): 
            # eu preciso saber se a frequencia de caracteres na janela é igual a frequencia da s1
            frequencia_s2[s2[r]] = frequencia_s2.get(s2[r], 0) + 1
            tam_janela = (r-l+1)
            if tam_janela > len(s1):
                frequencia_s2[s2[l]] = frequencia_s2.get(s2[l], 0) - 1
                l += 1
            frequencia_s2 = {k: v for k, v in frequencia_s2.items() if v != 0}
            if (frequencia_s1 == frequencia_s2):
                return True
        return False 
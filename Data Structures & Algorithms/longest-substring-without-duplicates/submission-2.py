class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        resultado = 0
        janela = set()
        for r in range(len(s)):
            while s[r] in janela:
                janela.remove(s[l])
                l += 1
            janela.add(s[r])
            resultado = max(resultado, len(janela))
            # print(f"janela {janela} em i {r}")
        return resultado
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        resultado = 0
        frequencia = {}
        for r in range(len(s)): 
            frequencia[s[r]] = frequencia.get(s[r], 0) + 1
            freq_max = max(frequencia.values())
            replaces = (r-l+1) - freq_max
            # print(f"Frequencia {frequencia} e Replaces {replaces} e frequencia max {freq_max}") 

            while replaces > k:
                frequencia[s[l]] = frequencia.get(s[l], 0) - 1
                l += 1
                freq_max = max(frequencia.values())
                replaces = (r-l+1) -freq_max
            resultado = max(resultado, replaces + freq_max)

        return resultado
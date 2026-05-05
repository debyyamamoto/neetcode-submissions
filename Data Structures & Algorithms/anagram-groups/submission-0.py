class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        guarda_palavras = defaultdict(list)
        resp = []
        for string in strs:
            string_ordenada = "".join(sorted(string))
            guarda_palavras[string_ordenada].append(string)
        for chave, valor in guarda_palavras.items():
            resp.append(valor)
        return resp      
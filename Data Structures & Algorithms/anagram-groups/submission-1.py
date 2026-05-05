class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        guarda_palavras = defaultdict(list)
        resp = []
        for string in strs:
            string_ordenada = "".join(sorted(string))
            guarda_palavras[string_ordenada].append(string)
        
        return list(guarda_palavras.values())  
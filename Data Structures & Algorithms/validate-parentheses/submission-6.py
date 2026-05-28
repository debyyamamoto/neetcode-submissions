class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        dicionario = {}
        dicionario[')'] = '('
        dicionario[']'] = '['
        dicionario['}'] = '{'
        # O(1)
        if len(s)%2 != 0:
            return False
        # O(n), sendo n o tamanho da string 
        for i in s:
            if i == "(" or i == "[" or i == "{":
                pilha.append(i)
            else:
                if len(pilha) != 0:
                    complemento = pilha.pop()
                else:
                    return False
                if complemento == dicionario[i]:
                    continue
                else:
                    return False
        if len(pilha) == 0:
            return True
        return False
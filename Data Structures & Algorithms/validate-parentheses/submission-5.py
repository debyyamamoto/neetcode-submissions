class Solution:
    def isValid(self, s: str) -> bool:
        pilha = deque()
        if len(s)%2 != 0:
            return False
        
        for i in s:
            if i == "(" or i == "[" or i == "{":
                pilha.append(i)
            else:
                if len(pilha) != 0:
                    complemento = pilha.pop()
                else:
                    return False
                if i == ")" and complemento == "(":
                    continue
                elif i == "]" and complemento == "[":
                    continue
                elif i == "}" and complemento == "{":
                    continue
                else:
                    return False
        if len(pilha) == 0:
            return True
        return False
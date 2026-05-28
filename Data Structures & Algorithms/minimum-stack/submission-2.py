class MinStack:

    def __init__(self):
        self.pilha = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.pilha)> 0:
            if val < self.pilha[-1][1]:
                min_atual = val
            else:
                min_atual = self.pilha[-1][1]
            self.pilha.append((val, min_atual))
        else:
            self.pilha.append((val, val))
    def pop(self) -> None:
        self.pilha.pop()

    def top(self) -> int:
        return self.pilha[-1][0]

    def getMin(self) -> int:
        return self.pilha[-1][1]
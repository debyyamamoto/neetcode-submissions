class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.tam = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.tam == self.capacity:
            self.resize()
        self.array[self.tam] = n
        self.tam += 1

    def popback(self) -> int:
        k = self.array[self.tam-1]
        self.array[self.tam-1] = None
        self.tam -= 1
        return k  

    def resize(self) -> None:
        antigo = self.array
        self.capacity = 2 * self.capacity
        new = [None] * self.capacity
        for i in range(self.getSize()):
            new[i] = antigo[i]
        self.array = new
        print(self.array)
        
    def getSize(self) -> int:
        return self.tam
    
    def getCapacity(self) -> int:
        return self.capacity
    
    def imprimir_array(self):
        print(self.array)



class Hissi:
    def __init__(self,alin,ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
    def kerros_ylös(self):
        self.kerros += 1
        print(f"mennään {self.kerros} kerros")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"mennään {self.kerros} kerros")
    def siirry_kerrokseen(self,kerros):
        while self.kerros < kerros and self.kerros < self.ylin:
            self.kerros_ylös()
        while self.kerros > kerros and self.kerros > self.ylin:
            self.kerros_alas()
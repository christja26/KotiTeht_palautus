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
class Talo:
    def __init__(self,alin,ylin,hissimäärä):
        self.alin = alin
        self.ylin = ylin
        self.hissimäärä = hissimäärä
        self.hissit = []
        for hissi in range(hissimäärä):
            self.hissit.append(Hissi(alin,ylin))
    def aja_hissiä(self,hissi,kohde):
        self.hissit[hissi - 1].siirry_kerrokseen(kohde)
    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)

rakennus = Talo(1,10,3)
rakennus.aja_hissiä(1,3)
rakennus.palohälytys()
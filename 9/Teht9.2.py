class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0
    def kiihdytä(self, kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

menopeli = Auto("ABC-123", 142)
print(f"rekkari: {menopeli.rekkari}, huippunopeus: {menopeli.huippunopeus}.")
menopeli.kiihdytä(30)
menopeli.kiihdytä(70)
menopeli.kiihdytä(50)
print(menopeli.nopeus)
menopeli.kiihdytä(-200)
print(menopeli.nopeus)
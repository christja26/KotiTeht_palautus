class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0
menopeli = Auto("ABC-123", 142)
print(f"rekkari: {menopeli.rekkari}, huippunopeus: {menopeli.huippunopeus}.")
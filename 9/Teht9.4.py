import random
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
    def kulje(self,tunnit):
        self.kuljettu += tunnit * self.nopeus
autot = []
kisa = True
for menopeli in range(10):
    autot.append(Auto(f"ABC-{menopeli+1}",random.randint(100,200)))
while kisa:
    for auto in autot:
        if auto.kuljettu > 10000:
            kisa = False
        else:
            auto.kiihdytä(random.randint(-10,15))
            auto.kulje(1)
for auto in autot:
    print(f"rekkari: {auto.rekkari} kulki: {auto.kuljettu}")
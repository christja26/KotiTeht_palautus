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
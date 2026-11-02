class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"nimi: {self.nimi}")
class Lehti(Julkaisu):
    def __init__(self,nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoitaja = kirjoittaja
        self.sivumäärä = sivumäärä
lehti = Lehti("Aku ankka", "aki hyyppä")
kirja = Kirja("hytti no. 6","rosa likson", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
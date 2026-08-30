annettu_luku = input("anna luku: ")
pienin_tiedetty_luku = int(annettu_luku)
suurin_tiedetty_luku = int(annettu_luku)
while annettu_luku != "":
    annettu_luku_lukuna = int(annettu_luku)
    if annettu_luku_lukuna < pienin_tiedetty_luku:
        pienin_tiedetty_luku = annettu_luku_lukuna
    elif annettu_luku_lukuna > suurin_tiedetty_luku:
        suurin_tiedetty_luku = annettu_luku_lukuna
    annettu_luku = input("anna luku: ")
print(f"pienin {pienin_tiedetty_luku}, suurin {suurin_tiedetty_luku}")
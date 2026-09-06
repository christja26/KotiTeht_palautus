nimet = set()
annettu = input("anna nimi: ")
while annettu != "":
    if annettu in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(annettu)
    annettu = input("anna nimi: ")
for nimi in nimet:
    print(nimi)
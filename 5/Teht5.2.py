annettu_luku = input("anna luku: ")
luvut = []
while annettu_luku != "":
    lukuna = int(annettu_luku)
    luvut.append(lukuna)
    annettu_luku = input("anna luku: ")
luvut = sorted(luvut, reverse=True)
for tulostettavat in range(5):
    print(luvut[tulostettavat])

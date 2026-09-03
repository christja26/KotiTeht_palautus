import random
def noppaheitto(tahkot):
    return random.randint(1,tahkot)
annettu = int(input("anna noppa tahkomäärä: "))
noppa = noppaheitto(annettu)
print(f"saatiin {noppa}")
while noppa != annettu:
    noppa = noppaheitto(annettu)
    print(f"saatiin {noppa}")
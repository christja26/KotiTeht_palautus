leiviskä = float(input("anna leiviskät: "))
naula = float(input("anna naulat: "))
luoti = float(input("anna luodit: "))
naula += leiviskä * 20
luoti += naula * 32
vastaus = luoti * 13.3
kilot = vastaus / 1000
grammat = vastaus - (int(kilot) * 1000)
print("Massa nykymittojen mukaan:")
print(f"{kilot:.2f} kilogrammaa")
print(f"{grammat:.2f} grammaa")
ajat = ("kevät", "kesä", "syksy", "talvi")
annettu = float(input("anna kuukausi numero: "))
if annettu >= 3 and annettu <= 5:
    print(ajat[0])
elif annettu >= 5 and annettu <= 8:
    print(ajat[1])
elif annettu >= 8 and annettu <= 10:
    print(ajat[2])
else:
    print(ajat[3])
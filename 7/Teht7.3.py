asemat = {}
annettu = int(input("toiminto: \n 1 = etsi asema \n 2 = lisää asema \n 3 = poistu : "))
while annettu != 3:
    if annettu == 1:
        print(asemat[input("etsittävän aseman koodi: ")])
    elif annettu == 2:
        koodi = input("anna ICAO-koodi: ")
        nimi  = input("anna nimi: ")
        asemat[koodi] = nimi
    annettu = int(input("toiminto: \n 1 = etsi asema \n 2 = lisää asema \n 3 = poistu : "))
tunnus = "python"
salasana = "rules"
kokeilukerrat = 5
while kokeilukerrat > 0:
    annettu_tunnus = input("tunnus: ")
    annettu_salasana = input("salasana: ")
    if annettu_tunnus == tunnus and annettu_salasana == salasana:
        print("Tervetuloa.")
        break
    else:
        print("Pääsy evätty.")
        kokeilukerrat -= 1
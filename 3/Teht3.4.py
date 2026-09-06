vuosi = int(input("anna vuosiluku: "))
vuosi_karkaa = False
if vuosi % 4 == 0:
    vuosi_karkaa = True
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        vuosi_karkaa = True
    else:
        vuosi_karkaa = False
print(f"annettu vuosi {["ei ole","on"][vuosi_karkaa]} karkausvuosi.")
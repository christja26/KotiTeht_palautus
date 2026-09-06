kokonaisluku = int(input("anna kokonaisluku: "))
alkuluku = True
for luku in range(1,kokonaisluku):
    if kokonaisluku % luku == 0:
        if luku == 1:
            continue
        elif luku == kokonaisluku:
            break
        else:
            alkuluku = False
if alkuluku:
    print("alkuluku tuo kyllä on")
else:
    print("alkuluku tuo ei ole")
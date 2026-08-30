import random
arpakuutiot = int(input("anna arpakuutiot: "))
summa = 0
for heitto in range(arpakuutiot):
    summa += random.randint(1,6)
print(f"heitettiin {arpakuutiot} määrä arpakuutioita, saatiin {summa}.")
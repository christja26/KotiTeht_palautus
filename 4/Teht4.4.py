import random
arvattava = random.randint(1, 10)
while True:
    arvaus = int(input("arvaa luku välillä 2-10: "))
    if arvaus == arvattava:
        break
    else:
        print("väärä luku")
        if arvaus > arvattava:
            print("liian suuri.")
        else:
            print("liian alhainen")
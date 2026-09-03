import random
def noppaheitto():
    return random.randint(1,6)
noppa = noppaheitto()
print(f"saatiin {noppa}")
while noppa != 6:
    noppa = noppaheitto()
    print(f"saatiin {noppa}")
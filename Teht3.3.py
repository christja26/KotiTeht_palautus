sukupuoli = input("anna sukupuoli (M / N) : ")
hemoglobiini = int(input("anna hemoglobiini: "))
if sukupuoli == "M":
    if hemoglobiini >= 134 and hemoglobiini <= 195:
        print("hemoglobiini normaali.")
    else:
        if hemoglobiini < 134:
            print("hemoglobiini alhainen.")
        if hemoglobiini > 195:
            print("hemoglobiini korkea.")
else:
    if hemoglobiini >= 117 and hemoglobiini <= 175:
        print("hemoglobiini normaali.")
    else:
        if hemoglobiini < 117:
            print("hemoglobiini alhainen.")
        if hemoglobiini > 175:
            print("hemoglobiini korkea.")
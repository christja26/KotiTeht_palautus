pituus = int(input("anna kuhan pituuden senttimetreinä: "))
if pituus < 37:
    print("takas järveen, kuha on alamittainen.")
    print(f"{37 - pituus}cm pyyntimitasta puuttuu.")
else:
    print("täydellistä.")
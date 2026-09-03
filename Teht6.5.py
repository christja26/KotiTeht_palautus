def parilliset(lista):
    parilliset = []
    for numero in lista:
        if numero % 2:
            continue
        else:
            parilliset.append(numero)
    return parilliset
esim = [1,2,3,4,5,6]
print(esim)
print(parilliset(esim))
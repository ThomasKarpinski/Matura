with open("cyfry.txt", "r") as plik:
    cyfry = [i.strip() for i in plik]

    """a)"""
    licznik = 0
    for i in cyfry:
        i = int(i)
        if i % 2 == 0:
            licznik += 1
    print(licznik)

    """b)"""
    l = []
    for cyfra in cyfry:
        suma = 0
        for znak in cyfra:
            suma += int(znak)
        l.append(suma)
    print(cyfry[l.index(max(l))],
          cyfry[l.index(min(l))])

    """c)"""
    for liczba in cyfry:
        licznik2 = 1
        for s in range(1, len(liczba)):
            if int(liczba[s]) > int(liczba[s - 1]):
                licznik2 += 1
        if licznik2 == (len(liczba)):
            print(liczba)

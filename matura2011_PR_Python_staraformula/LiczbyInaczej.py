with open("liczby (1).txt", "r") as plik:
    liczby = [i.rstrip() for i in plik]


    def horner_t(a, p):
        h = 0
        for i in a:
            if ord(i) >= 65:
                h = h * p + ord(i) - 55  # A to 65 w ascii lecz A ma wartość 10 w systemie hex
            else:
                h = h * p + int(i)
        return h

    """zad_a"""
    licznik = 0
    for liczba in liczby:
        if liczba[-1] == '0':
            licznik += 1
    print(licznik)

    """zad_b"""
    maxy = []
    for liczba in liczby:
        if len(liczba) == 16:
            maxy.append(liczba)

    kon = [horner_t(i, 2) for i in maxy]
    print(max(kon))

    """zad_c"""
    dl = [i for i in liczby if len(i) == 9]
    print(len(dl))
    suma = 0
    for i in dl:
        suma += horner_t(i, 2)
    print(bin(suma))

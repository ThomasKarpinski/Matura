def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


with open("liczby.txt", "r") as plik:
    mab = [[int(i) for i in j.split()] for j in plik]

    """3.3"""
    licznik = 0
    for i in mab:
        if pierwsza(i[0]):
            licznik += 1
    print(licznik)

    """3.4"""
    licznik_2 = 0
    for i in mab:
        if nwd(i[1], i[0]) == 1:
            licznik_2 += 1
    print(licznik_2)

    """3.5"""
    lista_trojek = set()
    for wiersz, i in enumerate(mab):
        m = i[0]
        for j in range(0, m - 1):
            licz = 0
            if (i[1] ** j) % m == i[2]:
                licz = 1
                lista_trojek.add(wiersz)
                if licz == 1:
                    licz = 0
                    break

    print(len(lista_trojek))

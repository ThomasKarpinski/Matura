from math import sqrt, ceil


def zaszyfruj(tekst):
    d = len(tekst)
    n = ceil(sqrt(d))

    tablica = [[] for i in range(n)]

    j = 0
    for wiersz in tablica:
        for i in range(n):
            if i + j < d:
                wiersz.append(tekst[i + j])
            else:
                wiersz.append('_')
        j += n

    szyfr = [wiersz[i] for i in range(n) for wiersz in tablica]

    return szyfr


print(zaszyfruj(*['algorytm_przestawieniowy']))

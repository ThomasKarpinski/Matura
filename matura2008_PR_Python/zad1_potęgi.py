import datetime

"""wersja 1"""
start = datetime.datetime.now()


def zad_b(k):
    wynik = 1
    if k >= 0:
        wynik = (2 ** k) % 10
    return wynik


czas_wykonania = datetime.datetime.now() - start
print(zad_b(15), czas_wykonania)

"""wersja 2"""


def zad_b2(k):
    if k == 0:
        return 1
    else:
        r = k % 4
        if r == 0:
            return 6
        elif r == 1:
            return 2
        elif r == 2:
            return 4
        elif r == 2:
            return 8


def zad_c(a, n):
    p = a
    while n > 1:
        p *= p
        n //= 2
    return p


print(zad_c(2, 4))

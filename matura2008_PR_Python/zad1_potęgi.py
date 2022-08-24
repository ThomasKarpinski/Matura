import datetime

start = datetime.datetime.now()
def zad_b(k):
    wynik = 1
    if k >= 0:
        wynik = (2 ** k) % 10
    return wynik


czas_wykonania = datetime.datetime.now() - start
print(zad_b(15), czas_wykonania)

def zad_c(a, n):
    p = a
    while n > 1:
        p *= p
        n //= 2
    return p


print(zad_c(2, 4))

"""z.1."""


def czyn(liczba):
    x = 2
    lista_czynnikow = []
    while x * x <= liczba:
        if liczba % x == 0:
            if x % 2 == 1:
                lista_czynnikow.append(x)
            else:
                return False
            liczba /= x
        else:
            x += 1
    if liczba > 1:
        lista_czynnikow.append(liczba)
    czynniki = set(lista_czynnikow)
    if len(czynniki) == 3:
        return True
    else:
        return False


with open("liczby (1).txt") as plik:
    wynik = 0
    for liczba in plik:
        liczba = int(liczba)
        if czyn(liczba):
            wynik += 1
print(wynik)

"""z.2."""

with open("liczby (1).txt") as plik:
    wynik = 0
    for i in plik:
        i = int(i)
        suma = i + int(str(i)[::-1])
        if suma == int(str(suma)[::-1]):
            wynik += 1
    print(wynik)

"""z.3."""


def iloczyn_cyfr(y):
    l = []
    s = 0
    for i in y:
        l.append(i)
    for j in l:
        j = int(j)
        s += j
    return s


f = open("liczby (1).txt").read()
plik = f.split('\n')

for i in plik:
    x = iloczyn_cyfr(i)
    moc = 0
    while moc <= 8:
        iloczyn_cyfr(i)
        print(f'moc {moc} liczba {i}')
        moc += 1

from math import sqrt


def _isPrime(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


with open("liczby.txt", "r") as plik:
    liczby = [int(i.strip()) for i in plik]

    lista = []
    for liczba in liczby:
        pierwiastek = sqrt(liczba)
        p = int(pierwiastek)
        if p == pierwiastek:
            if _isPrime(pierwiastek):
                lista.append(liczba)
                print(liczba)

    print(len(lista))

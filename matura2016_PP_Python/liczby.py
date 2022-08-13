lista_liczb_pierwszych = []


def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    lista_liczb_pierwszych.append(n)
    return True


with open('dane_6.txt') as plik:
    lista_liczb = []
    lista = []
    for linia in plik:
        liczba = linia.strip().split()
        liczba = list(liczba)
        liczba = ''.join(liczba)
        liczba = int(liczba)
        lista_liczb.append(liczba)
        if pierwsza(liczba) is True:
            lista.append(1)
print(lista.count(1))  # ilość liczb pierwszych

najmniejsza = None  # sprawdzanie największej i najmniejszej liczby pierwszej w pliku
najwieksza = None
for i in lista_liczb_pierwszych:

    if najmniejsza is None or najmniejsza > i:
        najmniejsza = i

    if najwieksza is None or najwieksza < i:
        najwieksza = i

print(f"najmniejsza liczba to: {najmniejsza}")
print(f"największa liczba to: {najwieksza}")

licznik = 0
first = 0
second = 0
for j in range(len(lista_liczb) - 1):
    first = lista_liczb[j]
    second = lista_liczb[j + 1]
    if first + 2 == second or first - 2 == second:
        licznik += 1
        print(first, second)
print(f"ilość liczb bliźniaczych: {licznik}")

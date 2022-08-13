"""z.21"""
with open("dzielniki.txt") as file:
    counter = 0
    listOfNumbers = []
    for number in file:
        number = int(number)
        if number < 1000:
            counter += 1
            listOfNumbers.append(number)
print(f"ilość liczb mniejszych od 1000: {counter}, dwie ostatnie takie liczby: {listOfNumbers[-1]} {listOfNumbers[-2]}")

"""z.22"""


def factor(n):

    d = 1
    lista = []
    while d * d <= n:
        if d * d == n:
            lista.append(d)
        if n % d == 0:
            lista.append(d)
            lista.append(n // d)
        d += 1
    return lista


with open("dzielniki.txt") as file:
    for number in file:
        number = int(number)
        if len(factor(number)) == 18:
            print(f"wymagane liczby: {number}; lista dzielników: {sorted(factor(number))}")

"""z.23"""
with open("dzielniki.txt") as file:
    listaWszystkichLiczb = []
    for number in file:
        number = int(number)
        listaWszystkichLiczb.append(number)
    sito1 = list(filter(lambda num: num % 2 != 0, listaWszystkichLiczb))
    sito2 = list(filter(lambda num: num % 3 != 0, sito1))
    primaryNumbers = list()
    dividers = 0

    for i in range(0, len(sito2)):
        for a in range(10, 101):
            if sito2[i] % a == 0:
                dividers += 1
                break
        if dividers == 0:
            primaryNumbers.append(sito2[i])
            dividers = 0
print(f"Najwieksza wzglednie pierwsza: {str(max(primaryNumbers))}")

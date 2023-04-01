import operator
import functools


def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def czy_trojkat_p(a, b, c):
    return (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)


with open("trojki.txt", "r") as plik:
    trojki = [i.split() for i in plik]
# print(trojki)
trojki_int = []
for trojka in trojki:
    result = list(map(lambda x: int(x), trojka))
    trojki_int.append(result)

# print(trojki_int)

"""3.1"""
print("zadanie 1 \n")
for trojka in trojki_int:
    a = str(trojka[0])
    b = str(trojka[1])
    a = [*a]
    b = [*b]
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    p = functools.reduce(operator.add, a)
    d = functools.reduce(operator.add, b)
    if p + d == trojka[2]:
        print(trojka)

"""3.2"""
print("zadanie 2 \n")
for trojka in trojki_int:
    if pierwsza(trojka[0]) and pierwsza(trojka[1]):
        if trojka[2] == trojka[0] * trojka[1]:
            print(trojka)

"""3.3"""
print("zadanie 3 \n")
for i in range(len(trojki_int)):
    if czy_trojkat_p(trojki_int[i][0], trojki_int[i][1], trojki_int[i][2]) and\
            czy_trojkat_p(trojki_int[i+1][0], trojki_int[i+1][1], trojki_int[i+1][2]):
        print(trojki_int[i],trojki_int[i+1])

"""3.4"""
print("zadanie 4 \n")
licznik = 0
liczba_jednek = []
parzyste = []
for trojka in trojki_int:
    result = list(map(lambda x: bin(x)[2::], trojka))
    result = ("").join(result)
    # print(result)
    if (ilosc := result.count('1')) % 2 == 0:
        licznik += 1
        liczba_jednek.append(ilosc)
        parzyste.append(result)
print(f"Liczba trójek: {licznik}")

print("Wiersze z największą ilością jedynek:")
najwiecej = max(liczba_jednek)
counter = 0
for i in liczba_jednek:
    if i == najwiecej:
        counter += 1
print(counter)
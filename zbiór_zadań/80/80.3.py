from itertools import combinations

with open("dane_trojkaty.txt", "r") as plik:
    liczby = [int(i) for i in plik]


def czy_trojkat(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


result = list(combinations(liczby, r=3))
nie_przyst = []
for i in result:
    if czy_trojkat(i[0], i[1], i[2]):
        nie_przyst.append(i)
print(len(set(nie_przyst)))

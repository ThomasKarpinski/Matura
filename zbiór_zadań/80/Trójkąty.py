from itertools import combinations
def czy_trojkat_p(a, b, c):
    return (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)

def czy_trojkat(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


with open("dane_trojkaty.txt", "r") as plik:
    liczby = [int(i) for i in plik]

"""80.1"""
# print(liczby)
for i in range(len(liczby)-2):
    if czy_trojkat_p(liczby[i], liczby[i+1], liczby[i+2]):
        print(liczby[i], liczby[i+1], liczby[i+2])

"""80.2"""

result = list(combinations(liczby, r=3))
obwody = []
for i in result:
    if czy_trojkat(i[0], i[1], i[2]):
        ob = sum(i)
        obwody.append(ob)
print(max(obwody))

"""80.3"""
nie_przyst = []
for i in result:
    if czy_trojkat(i[0], i[1], i[2]):
        nie_przyst.append(i)
print(len(set(nie_przyst)))

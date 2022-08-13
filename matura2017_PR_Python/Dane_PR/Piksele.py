from numpy import matrix

with open("dane.txt", "r") as plik:
    piksele = [[int(i) for i in j.split()] for j in plik]

'''6.1 - rozwiązanie laika'''
maksimum = minimum = piksele[0][0]
for i in piksele:
    for j in i:
        if j > maksimum:
            maksimum = j
        if j < minimum:
            minimum = j
print(maksimum, minimum)

'''6.1 - rozwiązanie z krotkami składanymi'''
maks = max(max(i) for i in piksele)
mini = min(min(i) for i in piksele)
print(maks, mini)

'''6.1 - trzeci sposób na zadanie'''
for i in piksele:
    maksimum = max(maksimum, *i)
    minimum = min(minimum, *i)
print(maksimum, minimum)

'''6.1 z wykorzystaniem biblioteki numpy'''


def numpy(dane):
    dane = matrix(dane)
    return dane


print("numpy:", numpy(piksele).max(), numpy(piksele).min())

'''6.2'''
wierszy = len(piksele) - len([i for i in piksele if i == i[::-1]])
print(wierszy)

'''6.3'''


def kontrast(a, b):
    return abs(a - b) > 128


k = 0
for i in range(200):
    for j in range(320):
        if i > 0 and kontrast(piksele[i - 1][j], piksele[i][j]):
            k += 1
        elif i < 199 and kontrast(piksele[i + 1][j], piksele[i][j]):
            k += 1
        elif j > 0 and kontrast(piksele[i][j - 1], piksele[i][j]):
            k += 1
        elif j < 319 and kontrast(piksele[i][j + 1], piksele[i][j]):
            k += 1
print(k)

'''6.4'''
maximumKol = 1
for i in range(320):
    kol = 1
    for j in range(1, 200):
        if piksele[j][i] == piksele[j - 1][i]:
            kol += 1
            maximumKol = max(maximumKol, kol)
        else:
            kol = 1
print(maximumKol)

'''6.4 - krótszy sposób'''
piksele = list(zip(*piksele[::-1]))
wynik = []
for i in piksele:
    k = 1
    wynik += [(k := k + 1) if i[j] == i[j - 1] else (k := 1) for j in range(1, len(i))]
print(max(wynik))

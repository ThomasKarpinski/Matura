plik1 = open("dane1.txt", "r")
plik2 = open("dane2.txt", "r")

dane1 = [[int(i) for i in j.split()] for j in plik1]
dane2 = [[int(i) for i in j.split()] for j in plik2]

'''4.1'''
licznik = 0
for row in range(1000):
    if dane1[row][-1] == dane2[row][-1]:
        licznik += 1
print(licznik)

'''4.2'''


def even(n):
    if n % 2 == 0:
        return True
    return False


licznik1 = []
licznik2 = []
for count, row in enumerate(dane1):
    if len(d1 := [i for i in row if even(int(i)) is True]) == 5:
        licznik1.append(count)

for count, row in enumerate(dane2):
    if len(d2 := [i for i in row if even(int(i)) is True]) == 5:
        licznik2.append(count)

print(len(set(licznik1) & set(licznik2)))

'''4.2 - wersja druga'''
licz = 0
for i in range(len(dane1)):
    p1 = p2 = 0
    for j in range(10):
        if int(dane1[i][j]) % 2 == 0:
            p1 += 1
        if int(dane2[i][j]) % 2 == 0:
            p2 += 1
    if p1 == p2 == 5:
        licz += 1
print(licz)

'''4.3'''
counter = []
for row in (range(1000)):
    if d1 := set(dane1[row]) == (d2 := set(dane2[row])):
        counter += [row + 1]
print(len(counter), counter)

'''4.4'''
for i in range(len(dane1)):
    i1 = i2 = 0
    dane3 = []
    while (i1 < 10) and (i2 < 10):
        if dane1[i][i1] <= dane2[i][i2]:
            dane3 += [dane1[i][i1]]
            i1 += 1
        else:
            dane3 += [dane2[i][i2]]
            i2 += 1
    if i1 > i2:
        dane3 += dane2[i][i2:]
    if i2 > i1:
        dane3 += dane1[i][i1:]
    print(dane3)

plik1.close()
plik2.close()

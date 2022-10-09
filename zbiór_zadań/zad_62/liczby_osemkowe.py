plik1 = open("liczby1.txt", "r")
plik2 = open("liczby2.txt", "r")

liczby1 = [int(i) for i in plik1]
liczby2 = [int(i) for i in plik2]
liczby2_2 = [oct(i)[2:] for i in liczby2]

"""1"""
maksymalna = 0
minimalna = min(liczby1)
miejsce = 0
for count, liczba in enumerate(liczby1):
    if liczba > maksymalna:
        maksymalna = liczba
        miejsce = count
print(maksymalna, miejsce)
print(minimalna, liczby1.index(minimalna))

"""2"""
mx = 1
length = 1
tab = liczby2
n = len(liczby2)
start = n
prev = start
ms = start
for number in range(1, n):
    if tab[number] < tab[number - 1]:
        if length > mx:
            ms = start
            mx = length
        start = number
        prev = start
        length = 1
    else:
        length += 1
        prev = number

print(mx, liczby2[ms])

"""3"""
rowne = 0
wieksze = 0
for i in range(1000):
    if liczby2_2[i] == str(liczby1[i]):
        rowne += 1
    if liczby2_2[i] < str(liczby1[i]):
        wieksze += 1
print(rowne, wieksze)

"""4"""
szostki_o = 0
szostki_d = 0
for j in range(1000):
    if '6' in liczby2_2[j]:
        l1 = liczby2_2[j].count('6')
        szostki_o += l1
    if '6' in str(liczby2[j]):
        l2 = str(liczby2[j]).count('6')
        szostki_d += l2
print(szostki_o, szostki_d)

plik1.close()
plik2.close()

import datetime

with open("dane4.txt", "r") as plik:
    liczby = [int(i.strip()) for i in plik]

    '''4.1'''
luki = [abs(liczby[i] - liczby[i + 1]) for i in range(len(liczby) - 1)]
print(min(luki), max(luki))

'''4.2'''
ciagmax = 0
for i in range(len(liczby) - 1):
    ix = 1
    while i + ix < len(luki) and luki[i] == luki[i + ix]:
        if ix > ciagmax:
            ciagmax = ix
            start = i
        ix += 1
print(f"Długość:{ciagmax + 2}\nPoczątek:{liczby[start]}"
      f"\nKoniec:{liczby[start + ciagmax + 1]}")

'''4.3'''
krotnosci = max([luki.count(i) for i in set(luki)])
print(krotnosci)
najluk = [i for i in set(luki) if luki.count(i) == krotnosci]
print(najluk)

'''4.3 - szybsza wersja'''
from collections import Counter

zestawienie = Counter(luki).most_common()
print([i for i in zestawienie if i[1] == zestawienie[0][1]])

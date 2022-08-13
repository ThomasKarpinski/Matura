from math import log, gcd

with open("liczby.txt", "r") as plik:
    liczby = [int(i) for i in plik]

'''4.1 - wersja na piechotę'''
p3 = []
p3 = set(p3)
k = 0
l = 0
while k <= 100:
    if l <= 100000:
        l = 3 ** k
        p3.add(l)
    k += 1
p3.remove(177147)
print(p3)
licznik = 0
for liczba in liczby:
    if liczba in p3:
        licznik += 1
print(licznik)

'''4.1 - zgrabniejsza wersja z zastosowaniem logarytmów'''
wyn = [liczba for liczba in liczby if round(log(liczba, 3), 10) % 1 == 0]
print(len(wyn))

'''4.2'''


def silnia(num):  # musimy skorzystać z tego iteracyjnego sposobu, ponieważ rekurencja ma ograniczoną ilość zagnieżdżeń
    s = 1
    for i in range(2, num + 1):
        s *= i
    return s


liczby_s = [str(i) for i in liczby]

for liczba in liczby_s:
    suma = sum([silnia(int(cyfra)) for cyfra in liczba])  # silnia albo z biblioteki math albo z własnej funkcji
    if suma == int(liczba):
        print(liczba, end=' ')
print("\n")

'''4.3'''
ciagmax = 0
for i in range(len(liczby) - 1):
    NDWciagu, ix = liczby[i], 1                     # NDWciagu - wartość pierwszej liczby ciągu
    while (i + ix < len(liczby)) and NDWciagu > 1:  # pętla zakończy się, gdy osiągnie wartość 1 lub gdy osiągnie koniec listy
        if ix > ciagmax:
            ciagmax, start, NDWmax = ix, liczby[i], NDWciagu    #jeśli znajdziemy dłuższy ciąg od aktualnego to podmienia warość na większą
        NDWciagu = gcd(NDWciagu, liczby[i + ix])    # użyłem tutaj gotowej funkcji gcd
        ix += 1                                     # liczby[i + ix] - "i-ta" liczba
print(f"Pierwsza liczba ciągu: {start}, długość ciągu: {ciagmax}, dzielnik: {NDWmax}")

with open("pary.txt", "r") as plik:
    pary = [i.split() for i in plik]
liczby = [int(i[0]) for i in pary]
slowa = [i[1] for i in pary]

'''4.1'''
def pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


p = [i for i in range(2, 100) if pierwsza(i)]
#print(p)
for i in liczby:
    if not i % 2:
        wynik = [[i, p[j], k] for j in range(len(p)) if pierwsza(k := i-p[j])]
        #print(wynik)

'''4.2'''
for i in slowa:
    fragment = maxfragment = i[0]
    for j in range(1, len(i)):
        if i[j] == i[j - 1]:
            fragment = i[j] * (len(fragment) + 1)
            if len(maxfragment) < len(fragment):
                maxfragment = fragment
            else:
                fragment = i[0]
    #print(maxfragment, len(maxfragment))

'''4.3'''
par = [[int(i[0]), i[1]] for i in pary]
rowne = []
for i in par:
    if i[0] == len(i[1]):
        rowne.append(i)
print(rowne)

lista_slow = []
for i in rowne:
    for j in range(1, len(i)):
        slowo = i[j]
        lista_slow.append(slowo)
print(lista_slow)

l = []
licznik = 1
for wyraz in lista_slow:
    k = [ord(i) for i in wyraz]
    for i in range(0, len(k)):
        if k[i] < k[i-1]:
            licznik += 1
        else:
            licznik = 1
    l.append((licznik))
print(max(l), wyraz)

'''4.3 - krótszy sposób'''
wyn = []
for i in pary:
    if int(i[0]) == len(i[1]):
        wyn += [(3 - len(i[0])) * "0" + i[0] + i[1]]
print(min(wyn))

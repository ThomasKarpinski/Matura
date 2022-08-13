with open("dzialki.txt", "r") as plik:
    dzialki = [i for i in plik]
liczba_dzialek = int((len(dzialki)+1)/31)

def wiersz(d, w):
    return dzialki[d*31+w][:-1]

'''nrD - indeks działki, nrW - indeks wiersza, nrZ - indeks znaku'''

'''4.1'''
dzialki_trawa = 0
for nrD in range(liczba_dzialek):
    trawa = 0
    for nrW in range(30):
        trawa += wiersz(nrD, nrW).count("*")
    if trawa / (30 * 30) >= 0.7:
        dzialki_trawa += 1
print(dzialki_trawa)

'''4.2'''
def dzialka(d):
    return dzialki[d * 31:d * 31 + 30]

dzialkiR = []
for nrD in range(liczba_dzialek):
    for nrW in range(30):
        dzialkiR.append(wiersz(nrD, 29 - nrW)[::-1]+"\n")
    dzialkiR.append("\n")

for nrD in range(liczba_dzialek - 1):
    for nrDR in range(nrD + 1, liczba_dzialek):
        if dzialka(nrD) == dzialkiR[nrDR * 31:nrDR * 31 + 30]:
            print(nrD+1, nrDR+1)

'''4.3'''
def znak(d, w, z):
    return dzialki[d*31+w][z]

bok = 0
nr_dzialek = ""
for nrD in range(liczba_dzialek):
    for kol in range(30):
        for wie in range(kol+1):
            if znak(nrD, kol, wie) == "X" or znak(nrD, wie, kol) == "X":
                if kol == bok:
                    nr_dzialek += str(nrD + 1) + " "
                elif kol > bok:
                    nr_dzialek = str(nrD + 1) + " "
                    bok = kol
                break
        if znak(nrD, kol, wie) == "X" or znak(nrD, wie, kol) == "X":
            break
print(nr_dzialek, "Bok: ",bok)
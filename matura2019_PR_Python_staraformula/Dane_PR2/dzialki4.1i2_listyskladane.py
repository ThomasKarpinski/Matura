with open("dzialki.txt", "r") as plik:
    dzialki = [i for i in plik]
liczba_dzialek = int((len(dzialki)+1)/31)

dzialki = [wiersz.split() for wiersz in dzialki]
dzialki = [dzialki[i:i+30] for i in range(0, len(dzialki) + 1, 31)]

dzialki_trawa = 0
for i in range(liczba_dzialek):
    if sum(["".join(dzialki[i][j]).count("*") for j in range(30)]) / 900 > 0.7:
        dzialki_trawa += 1
print(dzialki_trawa)

'''4.2'''
dzialkiR = [dz[::-1] for dz in dzialki]
dzialkiR = [[[wi[0][::-1]] for wi in dz] for dz in dzialkiR]

for nrD in range(liczba_dzialek):
    for nrDR in range(nrD+1, liczba_dzialek):
        if dzialki[nrD] == dzialkiR[nrDR]:
            print(nrD+1, nrDR+1)
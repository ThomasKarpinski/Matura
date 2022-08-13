with open("liczby.txt", "r") as plik:
    liczby = [i.strip() for i in plik]
osemkowy = [i[:-1] for i in liczby if i[-1] == "8"]

czworkowy = [i[:-1] for i in liczby if i[-1] == "4" and "0" not in i[:-1]]

parzyste = [i[:-1] for i in liczby if i[-1] == "2" and i[-2] == "0"]

wyn = [int(i, base=8) for i in osemkowy]
wyn = sum(wyn)

liczbyD = []
for i in liczby:
    liczbyD += [int(i[:-1], int(i[-1]))]

print(len(osemkowy), len(czworkowy), len(parzyste), wyn)
print(max(liczbyD), liczby[liczbyD.index(max(liczbyD))])
print(min(liczbyD), liczby[liczbyD.index(min(liczbyD))])

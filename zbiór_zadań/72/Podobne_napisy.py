with open("napisy.txt") as plik:
    napisy = [i.split() for i in plik]

# print(napisy)

"""72.1"""
wieksze = []
for wiersz in napisy:
    if (dl1 := len(wiersz[0])) >= 3 * (dl2 := len(wiersz[1])) or 3 * dl1 <= dl2:
        wieksze.append(wiersz)
# print(wieksze[0], len(wieksze))

"""72.2"""
for wiersz in napisy:
    licznik = 0
    for i in range(len(wiersz[0])):
        if wiersz[0][i] == wiersz[1][i]:
            licznik += 1
        else:
            break
    if len(wiersz[0]) == licznik:
        print(wiersz)

"""72.3"""
counter = 0
maxy = []
maks = counter
for wiersz in napisy:
    counter = 0
    for i in range(1, len(wiersz[0])+1):
        if wiersz[0][-i] == wiersz[1][-i]:
            counter += 1
        else:
            break
    print(counter)
    if counter > maks:
        maks = counter
print(maks)

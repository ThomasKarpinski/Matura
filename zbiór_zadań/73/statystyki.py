with open("tekst.txt", "r") as plik:
    tekst = [i.split(" ") for i in plik]

tekst = tekst[0]
# print(tekst)
"""73.1"""
licznik = 0
for slowo in tekst:
    ident = 0
    for i in range(len(slowo) - 1):
        if slowo[i] == slowo[i + 1]:
            ident += 1
    if ident == 2:
        licznik += 1
print(licznik)

tekst_z = ''.join(tekst)
# print(tekst_z)
"""73.2"""
for i in range(26):
    print(f"{chr(i + 65)}: {tekst_z.count(tekst_z[i])} "
          f"{round((((tekst_z.count(tekst_z[i])) / (len(tekst_z))) * 100), 2)}%")

"""73.3"""
samog = ['A', 'E', 'I', 'O', 'U', 'Y']
dlugosci = []
podslowa = []
maks = 0
for k, slowo in enumerate(tekst):
    dl = 0
    podslowo = ''
    for i in slowo:
        if i not in samog:
            dl += 1
            podslowo += i
        else:
            podslowa.append(podslowo)
            dlugosci.append(dl)
            maks = dl if dl > maks else maks
            dl = 0
            podslowo = ''
print(max(len(i) for i in podslowa))
print(dlugosci.count(4))
print(podslowa[dlugosci.index(4)])

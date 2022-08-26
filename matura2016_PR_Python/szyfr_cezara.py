'''6.1'''
with open("dane_6_1.txt") as plik_1:
    slowa = [i for i in plik_1]
    # print(slowa)
    klucz = 107
    odp = ""

    for slowo in slowa:
        for znak in slowo:
            szy_znak = chr((ord(znak) - 65 + klucz) % 26 + 65)
            odp += szy_znak
        odp += " "
    # print(odp)

    # rozwiazanie z listą składaną
    answer_1 = "".join(
        [chr((ord(znak) - 65 + klucz) % 26 + 65) if znak != "\n" else "\n" for slowo in slowa for znak in slowo])
    # print(answer_1)

'''6.2'''
'''with open("dane_6_2.txt") as plik_2:
    slowa = plik_2.readlines()
    odp = []
    for wiersz in slowa:
        wiersz = wiersz.split()
        slowo = wiersz[0]
        klucz = wiersz[1]
        for znak in slowo:
            odp += chr(((ord(znak) - 65 - int(klucz)) % 26 + 65))
        odp += "\n"
    print("".join(odp))'''

'''6.3'''
plik = open("dane_6_3.txt", "r")
slowa = plik.readlines()
odp = ""

def klucz(a,b):
    return (ord(a) - ord(b)) % 26

for wiersz in slowa:
    w, s = wiersz.split()
    for i in range(len(w)-2):
        if klucz(w[i-1], s[i-1]) != klucz(w[i], s[i]):
            if w not in odp:
                odp += w + "\n"
print(odp)
plik.close()
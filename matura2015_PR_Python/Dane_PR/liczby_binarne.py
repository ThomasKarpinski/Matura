plik = open("liczby.txt", "r")
tekst = plik.readlines()

'''4.1'''
licznik1 = 0
for wiersz in tekst:
    if wiersz.count("0") > wiersz.count("1"):
        licznik1 += 1
print(licznik1)

# lista składana
print(len([i for i in tekst if i.count("0") > i.count("1")]))

'''4.2'''
licznik_2 = licznik_8 = 0
for wiersz in tekst:
    dziesietne = int(wiersz.strip(), 2) # te zapis zmienia liczby z binarnego na dziesiętny
    if dziesietne % 2 == 0:
        licznik_2 += 1
    if dziesietne % 8 == 0:
        licznik_8 += 1
print(f"Liczba liczb podzielnych przez 2: {licznik_2} \n"
      f"Liczba liczb podzielnych przez 8: {licznik_8}")

# druga postać tego programu
li2 = li8 = 0
for wiersz in tekst:
    if wiersz.strip()[-3:] == "000":
        li8 += 1
    if wiersz.strip()[-1] == "0":
        li2 += 1
print(li2," ", li8)

'''4.3'''
lista = []
for wiersz in tekst:
    lista.append(int(wiersz.strip(), 2))
print(lista.index(max(lista))+1, " " , lista.index(min(lista))+1)

# za pomocą listy składanej
binarne = [int(wiersz.strip(), 2) for wiersz in tekst]
maksymalna = binarne.index(max(binarne))
minimalna = binarne.index(min(binarne))
print(f"{maksymalna+1}, {minimalna+1}")
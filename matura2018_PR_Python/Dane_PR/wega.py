plik = open("przyklad.txt", "r")

tekst = plik.readlines()

'''4.1'''
wynik = "".join([i[9] for i in tekst[39::40]])
print(wynik)

'''4.2'''
liczba_roznych_liter = tekst_wiersza = 0
for wiersz in tekst:
    litery = []
    for znak in wiersz[:-1]:  # stosujemy "[:-1]" aby pozbyć sie "\n" na końcu każdej lini
        if znak not in litery:
            litery.append(znak)
        if liczba_roznych_liter < len(litery):
            liczba_roznych_liter = len(litery)
            tekst_wiersza = wiersz[:-1]
print(tekst_wiersza, liczba_roznych_liter)

for wiersz in tekst:  # drugi sposób
    wiersz = wiersz[:-1]
    if liczba_roznych_liter < len(set(wiersz)):
        liczba_roznych_liter = len(set(wiersz))
        tekst_wiersza = wiersz
print(tekst_wiersza, liczba_roznych_liter)

for wiersz in tekst:  # trzeci sposób
    if liczba_roznych_liter < len(set(wiersz := wiersz[:-1])):
        # "operator morsa" przypisuję wartosć do zmiennej w warunku if
        liczba_roznych_liter = len(set(wiersz))
        tekst_wiersza = wiersz
print(tekst_wiersza, liczba_roznych_liter)

'''4.3'''
for wiersz in tekst:
    wiersz = wiersz[:-1]
    if ord(max(list(wiersz))) - ord(min(list(wiersz))) <= 10:
        print(wiersz)

for wiersz in tekst:  # drugi sposób
    wiersz = wiersz[:-1]
    if ord(max(*wiersz)) - ord(min(*wiersz)) <= 10:
        print(wiersz)

for wiersz in tekst:  # trzeci sposób
    tekst_wiersza = sorted(set(wiersz[:-1]))
    if ord(tekst_wiersza[-1]) - ord(tekst_wiersza[0]) <= 10:
        print(wiersz[:-1])

plik.close()

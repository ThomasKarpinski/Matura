with open("instrukcje.txt", "r") as plik:
    instrukcje = [i.strip() for i in plik]

    """4.1"""
    wynik = []
    for instrukcja in instrukcje:
        polecenie, litera = instrukcja[0:-2], instrukcja[-1]
        if polecenie == 'DOPISZ':
            wynik.append(litera)
        if polecenie == 'ZMIEN':
            wynik.pop()
            wynik.append(litera)
        if polecenie == 'USUN':
            wynik.pop()
        if polecenie == 'PRZESUN':
            if litera == 'Z':
                wynik[wynik.index(litera)] = 'A'
            else:
                Ascii = ord(litera) + 1
                zamieniony = chr(Ascii)
                wynik[wynik.index(litera)] = zamieniony

    print(wynik)

    """4.2"""


pokolenie = [[]]    # dwupoziomowa lista
with open("gra.txt", "r") as plik:
    for wiersz in plik:
        pokolenie[0] += [wiersz]    # wczytuję pierwszą planszę do pokoleń

    def sasiadow(w, k, p):
        """
        :param w: wiersz
        :param k: kolumna
        :param p: aktualne pokolenie
        :return: liczba żywych sąsiadów sprawdzanej komórki

        Treść zadania mówi, że komórki obu boków; góry i dołu sąsiadują ze sobą.
        Sprawdzając sąsiadów prawej strony czyli 19 element natrafimy na problem
        sprawdzenia zerowej komórki. Zabezpieczamy się przed tym biorąc resztę z
        dzielenia indeksu komórki przez 20 i analogicznie rozpatrujemy górne i dolne komórki.

        """
        ilu = 0
        for wi in range(-1, 2):
            for ki in range(-1, 2):
                if not(wi == ki == 0):
                    if pokolenie[p][(w+wi) % 12][(k+ki) % 20] == "X":
                        ilu += 1
        return ilu


    def ewolucja(w, k, p):
        """
        :param w: wiersz
        :param k: kolumna
        :param p: aktualne pokolenie

        funkcja sprawdza czy komórka w kolejnej generacji ma być żywa czy martwa
        """
        p -= 1  # sprawdzamy stan poprzedniego pokolenia
        ilu = sasiadow(w, k, p)
        if pokolenie[p][w][k] == "X" and (ilu == 2 or ilu == 3):
            return "X"
        elif pokolenie[p][w][k] == "." and ilu == 3:
            return "X"
        else:
            return "."


    def zywych(po):
        """
        :param po: pokolenie
        :return: zwraca liczbę żywych komórek w pokoleniu
        """
        suma = 0
        for i in po:
            suma += i.count("X")
        return suma


    for pok in range(1, 100):
        plansza = []
        for wi in range(12):
            wiersza = ""
            for ko in range(20):
                wiersz += ewolucja(wi, ko, pok)
            plansza += [wiersz]
        pokolenie += [plansza]

    '''5.1'''
    print(sasiadow(1, 18, 36))

    '''5.2'''
    print(zywych(pokolenie[1]))

    '''5.3'''
    i = 0
    while pokolenie[i] != pokolenie[i+1]:
        i += 1
    print(i+2, zywych(pokolenie[i+2])) # dodajemy dwa bo chcemy następne pokolenie i indeksujemy od 1

with open("szachy.txt", "r") as plik:
    szachy = [i.strip() for i in plik]

    plansze = []
    for i in range(0, len(szachy), 9):
        plansza = []
        for j in range(0, 8):
            plansza.append(szachy[i+j])
        plansze.append(plansza)

    # print(plansze)

    """1.1"""
    pusta_co_najmniej_jedna = 0
    najwiecej_pustych = 0

    for plansza in plansze:
        puste_na_danej_planszy = 0
        for kolumna in range(0, 8):
            pusta = True
            for wiersz in range(0, 8):
                if plansza[wiersz][kolumna] != '.':
                    pusta = False
                    break
            if pusta:
                puste_na_danej_planszy += 1
        if puste_na_danej_planszy > 0:
            pusta_co_najmniej_jedna += 1
            if puste_na_danej_planszy > najwiecej_pustych:
                najwiecej_pustych = puste_na_danej_planszy
    print(pusta_co_najmniej_jedna, najwiecej_pustych)

    """1.2"""
    pionki = ['k', 's', 'h', 'g', 'w', 'p']
    ile_plansz_w_rownowadze = 0
    ile_bierek_najmniej_w_rownowadze = 9999

    for plansza in plansze:
        czy_plansza_w_rownowadze = True
        plansza = ''.join(plansza)
        for pionek in pionki:
            if plansza.count(pionek) != plansza.count(pionek.upper()):
                czy_plansza_w_rownowadze = False
                break
        if czy_plansza_w_rownowadze:
            ile_plansz_w_rownowadze += 1
            ile_pol = len(plansza)
            ile_pustych = plansza.count('.')
            ile_bierek = ile_pol - ile_pustych
            if ile_bierek < ile_bierek_najmniej_w_rownowadze:
                ile_bierek_najmniej_w_rownowadze = ile_bierek
    print(ile_plansz_w_rownowadze, ile_bierek_najmniej_w_rownowadze)

    """1.3"""
    def ile_szachow(krol_symbol, wieza_symbol):
        ile_szachow = 0
        for plansza in plansze:
            czy_szachuje = False
            for wiersz in range(0, 8):
                for kolumna in range(0, 8):
                    if plansza[wiersz][kolumna] == krol_symbol:
                        # sprawdzenie w dół, górę itd
                        wiersz_w_gore = wiersz - 1
                        wiersz_w_dol = wiersz + 1
                        kolumna_w_prawo = kolumna + 1
                        kolumna_w_lewo = kolumna - 1

                        while wiersz_w_gore >= 0:
                            if plansza[wiersz_w_gore][kolumna] == wieza_symbol:
                                czy_szachuje = True
                                break
                            if plansza[wiersz_w_gore][kolumna] != '.':
                                break
                            wiersz_w_gore -= 1

                        while wiersz_w_dol <= 7:
                            if plansza[wiersz_w_dol][kolumna] == wieza_symbol:
                                czy_szachuje = True
                                break
                            if plansza[wiersz_w_dol][kolumna] != '.':
                                break
                            wiersz_w_dol += 1

                        while kolumna_w_prawo <= 7:
                            if plansza[wiersz][kolumna_w_prawo] == wieza_symbol:
                                czy_szachuje = True
                                break
                            if plansza[wiersz][kolumna_w_prawo] != '.':
                                break
                            kolumna_w_prawo += 1

                        while kolumna_w_lewo >= 0:
                            if plansza[wiersz][kolumna_w_lewo] == wieza_symbol:
                                czy_szachuje = True
                                break
                            if plansza[wiersz][kolumna_w_lewo] != '.':
                                break
                            kolumna_w_lewo -= 1

            if czy_szachuje:
                ile_szachow += 1

        return ile_szachow

    print(ile_szachow('K', 'w'))
    print(ile_szachow('k', 'W'))

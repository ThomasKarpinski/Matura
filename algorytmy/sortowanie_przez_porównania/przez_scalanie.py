def scalaj(t, lewy, prawy):
    """

    :param t: lista
    i_lewy: liczba stoją ca po lewej stronie sprawdzanego elementu
    i_prawy:liczba stojąca po prawej stronie środka danego wycinka
    """
    n = len(t)
    pom = []
    for i in range(n):
        pom.append(t[i])
    srodek = (lewy + prawy) // 2
    i = lewy
    i_lewy = lewy
    i_prawy = srodek + 1
    while i_lewy <= srodek and i_prawy <= prawy:
        if pom[i_lewy] < pom[i_prawy]:
            t[i] = pom[i_lewy]
            i_lewy += 1
        else:
            t[i] = pom[i_prawy]
            i_prawy += 1
        i += 1
    if i_lewy > srodek:
        while i_prawy <= prawy:
            t[i] = pom[i_prawy]
            i_prawy += 1
            i += 1
    else:
        while i_lewy <= srodek:
            t[i] = pom[i_lewy]
            i_lewy += 1
            i += 1


def sortuj(t, lewy, prawy):
    srodek = (lewy + prawy) // 2
    if lewy < srodek:
        sortuj(t, lewy, prawy)
    if srodek + 1 < prawy:
        sortuj(t, srodek + 1, prawy)
    scalaj(t, lewy, prawy)


def sortujprzezscalanie(t):
    n = len(t)
    sortuj(t, 0, n - 1)
    return t

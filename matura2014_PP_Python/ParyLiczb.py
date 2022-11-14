with open("PARY_LICZB.TXT", "r") as plik:
    pary = [i.strip() for i in plik]

    """a)"""
    licznik = 0
    for para in pary:
        para = list(para.split())
        try:
            if int(para[0]) % int(para[1]) == 0 or int(para[1]) % int(para[0]) == 0:
                licznik += 1
        except ZeroDivisionError or '':
            pass
    print(licznik)

    """b)"""
    def nwd(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a


    licznik2 = 0
    for para in pary:
        para = list(para.split())
        if nwd(int(para[0]), int(para[1])) == 1:
            licznik2 += 1
    print(licznik2)

    """c)"""
    licznik3 = 0
    for para in pary:
        para = list(para.split())
        l1 = map(lambda x: int(x), [*para[0]])
        l2 = map(lambda x: int(x), [*para[1]])
        if sum(l1) == sum(l2):
            licznik3 += 1
    print(licznik3)

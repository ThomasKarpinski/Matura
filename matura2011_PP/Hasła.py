with open("hasla.txt", "r") as plik:
    hasla = [i.strip() for i in plik]

    """a)"""
    p = [1 for i in hasla if len(i) % 2 == 0]
    np = len(hasla) - len(p)
    print('a)', len(p), np)

    """b)"""
    palindromy = [haslo for haslo in hasla if haslo[::-1] == haslo]
    print('b)', *palindromy)

    """c)"""
    print('c)')
    for haslo in hasla:
        for znak in range(len(haslo)):
            if ord(haslo[znak]) + ord(haslo[znak - 1]) == 220:
                print(haslo)

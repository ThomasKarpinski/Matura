with open("slowa.txt", "r") as plik:
    slowa = [i.strip() for i in plik]

    """a)"""
    for i in range(1, 13):
        print(f"Słów {i} -literowych jest {len([z for z in slowa if len(z) == i])}")

    """b)"""
    x = 0
    lista = []
    for slowo in slowa:
        print(f"{slowo} {slowa.count(slowo)} {slowa.count(slowo[::-1])}")

with open("dane.txt", "r") as plik:
    slowa = [i.strip() for i in plik]
    for count, slowo in enumerate(slowa):
        dl = len(slowo)
        pierwsza = slowo[:dl // 2]
        druga = slowo[dl // 2:]
        druga = druga[::-1]
        if pierwsza == druga:
            print(slowo, count)

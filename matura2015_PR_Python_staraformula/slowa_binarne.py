<<<<<<< HEAD
with open("slowa.txt", "r") as plik:
    slowa = [i.rstrip() for i in plik]
    """zad.1"""
    licznik = 0
    for slowo in slowa:
        if slowo.count('0') > slowo.count('1'):
            licznik += 1
    print(licznik)

    """zad.2"""
    licznik2 = 0
    for slowo in slowa:
        if slowo[0] == '1' or slowo.count('1') == 0:
            continue
        p = slowo.index('1')
        if slowo.count('0', p + 1) == 0:
            licznik2 += 1
    print(licznik2)

    """zad.3"""
    slowa_s = []
    licznik3 = 0
    kontener = []
    flaga = False
    for slowo in slowa:
        kontener.append(slowo)
    for i in range(25, 1, -1):
        for slowo in kontener:
            if (slowo.find(i*'0')) != -1:
                flaga = True
                slowa_s.append(slowo)
                licznik3 = i
        if flaga:
            break
    print(slowa_s, licznik3)
=======
"""zadanie drugi arkusz"""


class words():
    def __init__(self, f):
        self.f = open("slowa.txt", "r", encoding="utf-8")

    def zad_a(self):
        slowa = [i for i in self.f]
        licznik = 0
        for slowo in slowa:
            if slowo.count('0') > slowo.count('1'):
                licznik += 1
        return licznik


print(words.zad_a())
>>>>>>> 8f6e03b88a2d73895e83c86f82e62269d071eb75

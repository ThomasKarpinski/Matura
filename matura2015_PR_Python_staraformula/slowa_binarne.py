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

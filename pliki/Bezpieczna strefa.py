from math import gcd

"""1.2"""


def czy_otwiera(kod):
    kod = [str(i) for i in kod]
    lewa = ('').join(kod[0:2])
    prawa = ('').join(kod[2:4])
    lewa = ('').join(lewa)
    prawa = ('').join(prawa)
    if lewa[0] == '0':
        lewa = lewa[1]
    if prawa[0] == '0':
        prawa = prawa[1]
    lewa = int(lewa)
    prawa = int(prawa)
    if kod.count('0') > 1:
        return "ZAMKNIĘTE"
    else:
        if gcd(lewa, prawa) == 1:
            return "OTWARTE"
        else:
            return "ZAMKNIĘTE"


print(czy_otwiera([1, 3, 9, 1]))

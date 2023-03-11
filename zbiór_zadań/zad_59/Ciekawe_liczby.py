with open("liczby.txt", "r") as dane:
    liczby = [int(i) for i in dane]


# print(liczby)

def czynniki(a):
    d = 2
    l = []
    while a > 1:
        while a % d == 0:
            if d not in l:
                l.append(d)
            a //= d
        d += 1
    return l


"""59.1"""
'''licznik = 0
for wiersz in liczby:
    czy_p = 0
    if len(czyn := czynniki(wiersz)) == 3:
        if 2 not in czyn:
            licznik += 1'''

# print(licznik)

"""59.2"""


def odwracanie(liczba):
    l = 0
    while liczba > 0:
        l = l * 10 + liczba % 10
        liczba //= 10
    return l


licz = 0
for wiersz in liczby:
    if odwracanie(odwracanie(wiersz) + wiersz) == (odwracanie(wiersz) + wiersz):
        licz += 1
print(licz)

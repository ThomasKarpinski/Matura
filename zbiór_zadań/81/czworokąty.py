with open("wspolrzedne.txt") as plik:
    wspolrzedne = [i.split() for i in plik]

# print(wspolrzedne)

"""81.1"""
licznik = 0
for i in wspolrzedne:
    xa, ya, xb, yb, xc, yc = int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5])
    if xa > 0 and ya > 0 and xb > 0 and yb > 0 and xc > 0 and yc > 0:
        licznik += 1
print(licznik)

"""81.2"""
counter = 0


def prosta(a, b, c, d, e, f):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    global a1
    global a2
    global a3
    try:
        a1 = (b - a) / (d - c)
        a2 = (b - a) / (f - e)
        a3 = (d - c) / (f - e)
    except ZeroDivisionError:
        if a1 == a2 == a3:
            return True


for i in wspolrzedne:
    if prosta(i[0], i[1], i[2], i[3], i[4], i[5]):
        counter += 1
print(counter)

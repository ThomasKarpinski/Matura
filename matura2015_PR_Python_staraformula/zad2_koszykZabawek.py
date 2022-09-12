def zad2(mk, masa, cena):
    k = []
    n = len(masa)
    for j in range(n):
        k.append(0)
    w = 0
    for i in range(1, n):
        if mk >= masa[i]:
            k[i] = 1
            mk = mk - masa[i]
            w = w + cena[i]
        else:
            k[i] = 0
    return k


masa = [8, 4, 1, 2, 3, 5, 1]
cena = [320, 152, 37, 70, 99, 155, 30]
print(zad2(10, masa, cena))

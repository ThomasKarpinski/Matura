def dzielniki(n):

    d = 1
    l = []
    while d * d <= n:
        if d * d == n:
            l.append(d)
        if n % d == 0:
            l.append(d)
            l.append(n // d)
        d += 1
    return l


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


'''4.1'''
with open('liczby (1).txt') as plik:
    licznik = 0
    lista_dzielnikow = []
    l_nwd = []
    for linia in plik:
        linia = linia.strip().split()
        if int(linia[0]) < int(linia[1]) < int(linia[2]) and int(linia[0]) < int(linia[2]):
            licznik += 1
        lista_dzielnikow.append(dzielniki(int(linia[0])))
        lista_dzielnikow.append(dzielniki(int(linia[1])))
        lista_dzielnikow.append(dzielniki(int(linia[2])))
        l_nwd.append(max(lista_dzielnikow))
print(licznik)
'''4.2'''
with open('liczby (1).txt') as plik:
    suma = 0
    for linia in plik:
        linia = linia.strip().split()
        if nwd(int(linia[0]), int(linia[1])) > nwd(int(linia[1]), int(linia[2])):
            suma += nwd(int(linia[0]), int(linia[1]))
        else:
            suma += nwd(int(linia[1]), int(linia[2]))
print(suma)
'''4.3'''
with open('liczby (1).txt') as plik:
    suma_cyfr = 0
    for linia in plik:
        print(linia)
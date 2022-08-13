def ilosc_czynnikow(n):
    lista_czynnikow = []
    d = 2
    licznik = 0
    while n > 1:
        while n % d == 0:
            lista_czynnikow.append(d)
            n //= d
        d += 1
    for czynnik in range(len(lista_czynnikow)-1):
        if lista_czynnikow[czynnik] != lista_czynnikow[czynnik + 1]:
            licznik += 1
    return licznik+1


print(ilosc_czynnikow(int(input("Podaj liczbę "))))

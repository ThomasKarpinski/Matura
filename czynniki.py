def czynniki(n):
    lista_czynnikow = []
    d = 2
    while n > 1:
        while n % d == 0:
            lista_czynnikow.append(d)
            n //= d
        d += 1
    return lista_czynnikow


print(czynniki(int(input("Podaj liczbę "))))

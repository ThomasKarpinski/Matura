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

print(dzielniki(int(input("Podaj liczbę: "))))

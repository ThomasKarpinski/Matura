wspolczynniki = [2, -3, 1]
x = 3

wynik = wspolczynniki[0]
for i in range(1, len(wspolczynniki)):
    wynik = wynik * x + wspolczynniki[i]

print(wynik)
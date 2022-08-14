liczby = [2, 10, 12, 15, 20, 25, 30, 35]


# Mapy
def funkcja(x):
    return x + 2


wynik = map(funkcja, liczby)
print(list(wynik))  # funkcja nazwana

wynik2 = map(lambda x: x + 2, liczby)
print(list(wynik2))  # wykorzystanie funkcji lambda

# Filtry

wynik3 = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))

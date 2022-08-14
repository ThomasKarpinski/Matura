def funkcja(f, liczba):
    return f(liczba)


print(funkcja(lambda x: x * x, 3))  # sposób 1


def kwadrat(x):
    return x * x


print(kwadrat(5))  # sposób 2

wynik = (lambda x: x * x)(5)
print(wynik)  # sposób 3

lam = lambda x: x * x
print(lam(5))  # sposób 4

lam2 = lambda x, y: x * y  # więcej zmiennych
print(lam2(5, 3))

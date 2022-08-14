a = 79834
x = a
wynik = ''
while a > 0:
    x = a % 10
    a //= 10
    wynik += str(x)
wynik = int(wynik)
print(wynik)

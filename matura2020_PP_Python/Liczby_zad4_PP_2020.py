f = open("liczby (1).txt").read()
file = f.split('\n')
file = [int(x) for x in file]
"""4.1"""
ilosc = 0
print('4.1\n')
for number in file:
    if number % 2 != 0:
        ilosc += 1
print(ilosc)
"""4.2"""
print('4.2\n')


def suma_cyfr(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


for number in file:
    if suma_cyfr(number) == 11:
        print(number)
"""4.3"""
print('4.3\n')


def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


for number in file:
    if pierwsza(number) and 4000 < number < 5000:
        print(number)

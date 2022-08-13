def nwd(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    if b > 0:
        return nwd(b, a % b)
    else:
        return a


def suma_cyfr(n):
    """

    :param n:
    :return:
    """
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


with open("liczby (1).txt") as file:
    """4.1"""
    licznik = 0
    for i in file:
        b = i.split(' ')
        if int(b[0]) < int(b[1]) < int(b[2]):
            licznik += 1
    print(licznik)
with open('liczby (1).txt') as file:
    """4.2"""
    suma_nwd = 0
    for i in file:
        b = i.split(' ')
        suma_nwd += nwd(nwd(int(b[0]), int(b[1])), int(b[2]))
    print(suma_nwd)
f = open("liczby (1).txt").read()
file = f.split('\n')
"""4.3"""
max_suma_cyfr = 0
lines = 0
repeat = 0
for i in file:
    b = i.split(' ')
    if suma_cyfr(int(b[0])) + suma_cyfr(int(b[1])) + suma_cyfr(int(b[2])) > max_suma_cyfr:
        max_suma_cyfr = suma_cyfr(int(b[0])) + suma_cyfr(int(b[1])) + suma_cyfr(int(b[2]))
    if suma_cyfr(int(b[0])) + suma_cyfr(int(b[1])) + suma_cyfr(int(b[2])) == 35:
        lines += 1
for i in file:
    b = i.split(' ')
    if suma_cyfr(int(b[0])) + suma_cyfr(int(b[1])) + suma_cyfr(int(b[2])) == max_suma_cyfr:
        repeat += 1
print(max_suma_cyfr, lines, repeat)

def zad1_b(a):
    """
    :param a: liczba całkowita
    :return: zwraca liczbę b skojarzoną z a
    """
    if a > 1:
        d = []
        for i in range(1, a):
            if a % i == 0:
                d.append(i)
        suma = 0
        for j in d:
            suma += j
        return suma - 1
    return "NIE"


print(zad1_b(140))


def zad1_b_wersja2(a):
    b, b1 = 0, 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            b += i
    for i in range(2, b // 2 + 1):
        if b % i == 0:
            b1 += i
    if a == b1:
        print(b)
    else:
        print("NIE")


zad1_b_wersja2(140)

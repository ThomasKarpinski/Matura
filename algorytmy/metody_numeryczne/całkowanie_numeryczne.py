from math import fabs


def F(x):
    """
    :param x:
    :return: przykładowa funkcja
    """
    return x ** 2 - x - 3


def oblicz(p, q, n):
    """
    :param p: wartość na osi x
    :param q: wartość na osi y
    :param n: liczba naturalna (liczba prostokątów)
    :return: pole obszaru ograniczonego wykresem funkcji f(x) w przedziale [p,q]
    """
    dl = (q - p) / n
    s = 0
    for i in range(n):
        s += fabs(F(p + dl * i + dl / 2))
    return dl * s


print(oblicz(-2, 5, 30))

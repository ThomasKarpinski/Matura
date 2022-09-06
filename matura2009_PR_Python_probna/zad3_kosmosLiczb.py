"""program dodający liczby w tym samym systemie gdzie podstawa p i 2 <= p <= 9"""


def zad_b(a, b, n, p):
    """
    :param a: pierwsza liczba
    :param b: druga liczba
    :param n: ilość cyfr liczb
    :param p: podstawa systemu
    :return: wynik dodawania a i b
    """
    c = [0 for i in range(n + 1)]
    dalej = 0
    for i in range(n, -1, -1):
        pom = a[i] + b[i] + dalej
        c[i] = pom % p
        dalej = pom // p
    return c


print(zad_b([0, 1, 2, 2, 2], [0, 1, 0, 1, 1], 4, 4))

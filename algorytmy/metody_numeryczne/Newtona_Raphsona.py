from math import fabs


def pierwiastek(p, E, L):
    """

    :param p: liczba rzeczywista (podpierwiastkowa)
    :param E: liczba naturalna (maksymalna liczba iteracji)
    :param L: liczba rzeczywista (dokładność obliczeń)
    :return: przybliżona wartość pierwiastka kwadratowego z liczby
     p wyznaczona z dokładnością E lub po wykonaniu co najwyżej L iteracji:a
    """
    a, i = p, 0
    while fabs(a - p / a) > E and i < L:
        a = (a + p / a) / 2
        i += 1
    return a


print(pierwiastek(10, 0.00001, 50))

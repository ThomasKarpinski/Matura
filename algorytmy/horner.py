"""Algorytm hornera działający na stringu i algorytm działający na incie"""
from odwracanie_iczby import odwroc


def horner_t(a, p):
    """
    :param a: liczba jako tekst
    :param p: podstawa systemu liczby a
    :return: liczba w systemie dziesiętnym
    """
    h = 0
    for i in a:
        if ord(i) >= 65:
            h = h * p + ord(i) - 55  # A to 65 w ascii lecz A ma wartość 10 w systemie hex
        else:
            h = h * p + int(i)
    return h


print(horner_t('173', 8))


def horner_l(a, p):
    h = 0
    a = odwroc(a)
    while a > 0:
        h = h * p + a % 10
        a //= 10
    return h


print(horner_l(173, 8))

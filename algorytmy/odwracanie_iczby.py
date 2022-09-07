"""Program odwraca liczbę nie zamieniając na tekst, ale nie daje zera z przodu"""


def odwroc(a):
    """
    :param a: liczba jako int
    """
    w = 0
    while a > 0:
        w = a % 10 + w * 10
        a //= 10
    return w


#print(odwroc(11010))

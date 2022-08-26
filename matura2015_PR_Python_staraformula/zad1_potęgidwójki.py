def zad1_b(n):
    """
    :param n: dodatnia liczba całkowita
    :return: liczba różnych potęg liczby 2, których suma = n
    """
    lp = 0
    while n:
        lp += n % 2
        n //= 2
    return lp


print(zad1_b(18))

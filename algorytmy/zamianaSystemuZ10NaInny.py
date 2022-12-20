"""Program zamienia liczbę z systemu 10
 na dowolny inny system o podstawie p"""


def zamien10_p(liczba, p):
    """
    :param liczba w systemie 10
    :param p: podstawa dowolnego innego systemu
    :return: przekonwerterowana liczba
    """
    w = ''
    while liczba > 0:
        if liczba % p >= 10:
            w = chr(liczba % p + 55) + w
        else:
            w = str(liczba % p) + w
        liczba //= p
    return w


print(zamien10_p(415, 16))
print(hex(43))

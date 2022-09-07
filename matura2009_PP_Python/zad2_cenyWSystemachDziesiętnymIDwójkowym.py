def zad_b(s):
    """
    :param s: liczba w systemie dwójkowym z dwoma cyframi po przecinku
    :return: liczba w systemie dziesiętnym
    """
    wynik = 0
    k = 0.25
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ',':
            wynik += k*(ord(s[i]) - ord('0'))
            k *= 2
    return wynik


print(zad_b('10000111,01'))

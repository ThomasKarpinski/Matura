def sortuj(t):
    """
    n: długość listy

    :param t: lista
    :return: zwraca posortowaną listę
    """
    n = len(t)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if t[j] < t[k]:
                k = j
            t[k], t[i] = t[i], t[k]
    return t

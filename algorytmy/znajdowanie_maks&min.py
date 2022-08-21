def oblicz(t):
    """
    :param t: lista wartości
    :return: największa wartość w liście
    """
    maksimum = t[0]
    for k in t:
        if k > maksimum:
            maksimum = k
    return maksimum

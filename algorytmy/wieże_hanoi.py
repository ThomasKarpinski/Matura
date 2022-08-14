def oblicz(n, a, b, c):
    """

    :param n: liczba krążków
    :param a: palik A
    :param b: palik B
    :param c: palik C
    """
    if n > 0:
        oblicz(n - 1, a, c, b)
        print(a, "na ", b)
        oblicz(n - 1, c, b, a)


oblicz(4, "A", "B", "C")

"""Program zwraca największe pole prostokąta z podanych liczb, niepodzielnego przez p"""


def pole_p(A, p):
    """
    :param A: lista wartości
    :param p: liczba pierwsza
    :return: pole prostokąta
    """
    pierwsza, druga = 0, 0
    for i in A:
        if i % p != 0:
            if i > pierwsza:
                druga = pierwsza
                pierwsza = i
            elif i > druga:
                druga = i
    S = pierwsza * druga
    return S


print(pole_p([7, 5, 11, 33], 3))

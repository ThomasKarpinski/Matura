"""Program przedstawia tablicę dwuwymiarową uzupełnianą
według rekurencji ile(n-1,m-1)+ile(n-1,m)"""


def zad_c(n):
    """
    :param n: liczba kolumn i wierszy
    """
    dwu_wymiar = [[0 for kolumna in range(n + 1)]
                  for wiersz in range(n + 1)]
    for i in range(n + 1):
        dwu_wymiar[i][i] = 1
        dwu_wymiar[i][0] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dwu_wymiar[i][j] = dwu_wymiar[i - 1][j - 1] + dwu_wymiar[i - 1][j]
    for i in range(n + 1):
        print(dwu_wymiar[i])


zad_c(5)

def sortuj(t, lewy, prawy):
    i, j = lewy, prawy
    srodek = t[(lewy + prawy) // 2]
    while i <= j:
        while t[i] < srodek:
            i += 1
        while t[j] > srodek:
            j -= 1
        if i <= j:
            t[i], t[j] = t[j], t[i]
            i, j = i + 1, j - 1
    if lewy < j:
        sortuj(t, lewy, j)
    if prawy > i:
        sortuj(t, i, prawy)


def sortujszybko(t):
    n = len(t)
    sortuj(t, 0, n - 1)
    return t

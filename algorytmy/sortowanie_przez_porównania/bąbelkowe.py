def sortuj(t):
    n = len(t)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    return t

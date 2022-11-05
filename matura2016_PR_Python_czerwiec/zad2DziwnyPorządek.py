def maksymalna(lista, n):
    p = []
    np = []
    for i in range(n):
        if lista[i] % 2 == 0:
            p.append(lista[i])
        else:
            np.append(lista[i])
    if len(np) != 0:
        for i in range(len(np)):
            if np[i] > np[i - 1]:
                maks = np[i - 1]
                return maks
    else:
        for i in range(len(p)):
            if p[i] < p[i - 1]:
                maks = p[i - 1]
                return maks


print(maksymalna([3, 6, 1, 8, 11, 15, 20, 5, 70, 100, 1000], 11))

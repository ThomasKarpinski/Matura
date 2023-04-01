def sortuj(t):
    n = len(t)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    return t

print(sortuj([7,4,5,4,2,3,5,1,9]))
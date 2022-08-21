def sortuj(t):
    n = len(t)
    for i in range(1, n):
        pom = t[i]
        k = i - 1
        while k >= 0 and t[k] > pom:
            t[k + 1] = t[k]
            k -= 1
        t[k + 1] = pom
    return t

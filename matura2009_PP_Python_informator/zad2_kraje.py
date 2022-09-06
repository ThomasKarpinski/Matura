def oblicz(A, p):
    n = len(A)
    w = A[0]
    for i in range(1, n):
        w = w * p + A[i]
    return w


print(oblicz([2, 0, 7], 8))

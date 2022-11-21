"""zad1"""
def horner(C, d):
    h = 0
    for i in range(0, d, 1):
        h = h * 6 + int(C[-i - 1])
    return h


print(horner([0, 0, 0, 1], 4))

"""zad2"""
def tablice(n, k, A):
    T = [0 for i in range(k)]
    for i in range(n):
        pozycja = A[i]
        T[pozycja] += 1
        if pozycja > T[pozycja]:
            T.append(0)
    y = 1
    for j in range(1, k):
        if T[j] > T[y]:
            y = j
    return y, T


print(tablice(7, 4, [2, 3, 4, 2, 3, 1, 2]))

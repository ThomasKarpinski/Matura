a = [5, 1, 8, 9, 7, 2, 3, 11, 20, 15]
n = len(a)

def F(i):
    if i == n:
        return n
    j = F(i + 1)
    if a[i - 1] < a[j - 1]:
        return i
    else:
        return j


print(F(9))
print(F(7))
print(F(5))


def F_iter(i):
    indeks_min = i - 1
    for j in range(i, n):
        if a[j] < a[indeks_min]:
            indeks_min = j
    return indeks_min + 1


print(F_iter(5))
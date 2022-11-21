def kompresja(n, T):
    for i in range(n):
        if T[i] == T[i - 1]:
            T.pop(i)
        if T[i] != T[i - 1]:
            T.append('')
    return T, len(T) - 1


print(kompresja(10, [*'FFFYYYFFHA']))

def suma(n):
    n = str(n)
    n = [*n]
    s = 0
    for i in n:
        s += int(i)
    return s


def wsp(n):
    k = 0
    k = (n - suma(n)) // 9
    return k

def D(n):
    zlicz = 0
    while n > 1:
        if n % 2 == 0 and n > 1:
            n //= 4
            zlicz += 1
        if n % 2 != 0 and n > 1:
            n = 3 * n + 1
            zlicz += 1
    return zlicz + 1


print(D(31))

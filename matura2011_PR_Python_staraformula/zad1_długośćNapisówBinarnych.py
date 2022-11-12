"""a"""


def sklej(n):
    print("sklej (", n, ")")
    if n == 1:
        return 0
    if n % 2 == 0:
        return n - 1 + 2 * sklej(n // 2)
    else:
        return n - 1 + sklej((n - 1) // 2) + sklej((n + 1) // 2)


# sklej(7)

"""b"""
for i in range(1, 7):
    print("n: ", i, "sklej(n): ", sklej(i))

"""c"""
print("c)")


def sklej_iter(n):

    pom = [0 for i in range(n + 1)]

    for i in range(2, n + 1):
        if i % 2 == 0:
            pom[i] = i - 1 + 2 * pom[i // 2]
        else:
            pom[i] = i - 1 + pom[(i - 1) // 2] + pom[(i + 1) // 2]
    return pom


print(sklej_iter(7))

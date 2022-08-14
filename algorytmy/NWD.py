def nwd_for_3_args(a, b, c):
    if a == b and a == c: return a
    if a > b: return nwd_for_3_args(a - b, b, c)
    if a > c: return nwd_for_3_args(a - c, b, c)
    if b > a: return nwd_for_3_args(a, b - a, c)
    if b > c: return nwd_for_3_args(a, b - c, c)
    if c > a: return nwd_for_3_args(a, b, c - a)
    if c > b: return nwd_for_3_args(a, b, c - b)


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print(nwd(54,45))

no = [6, 3, 9]
print("\n", no[0], no[1], no[2],
      "nwd (3):", nwd_for_3_args(no[0], no[1], no[2]))

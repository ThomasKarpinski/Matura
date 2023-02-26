def NWD(a, b):
    if b > 0:
        return NWD(b, a % b)
    else:
        return a


def nwd_kilka(l):
    nwd = l[0]
    for i in range(1, len(l)):
        nwd = NWD(nwd, l[i])
    return nwd


def NWW(a, b):
    return (a * b) / NWD(a, b)


def NWD_odej(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


print(nwd_kilka([36, 24, 72, 150]))

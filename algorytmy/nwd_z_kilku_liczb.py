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


print(nwd_kilka([36, 24, 72, 150]))

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a
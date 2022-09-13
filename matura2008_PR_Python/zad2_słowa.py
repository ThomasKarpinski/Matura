def REG_2(w):
    n = len(w)
    if n == 1:
        return True
    if n > 1 and n % 2 != 0:
        return False
    if n > 1 and n % 2 == 0:
        w1 = w[0:(n // 2)]
        w2 = w[(n // 2)::]
        if w1 not in w2:
            return False
        return REG_2(w1)


print(REG_2('aaaaaaaa'))


def REG_3(w):
    n = len(w)
    if n == 1:
        return True
    if n > 1 and n % 3 != 0:
        return False
    if n > 1 and n % 3 == 0:
        w1 = w[0:(n // 3)]
        w2 = w[(n // 3):((n // 3) + 3)]
        w3 = w[(n // 3):-1]
        if w1 not in w3 and w1 not in w2:
            return False
        return REG_3(w1)


print(REG_3('aaaabaaba'))
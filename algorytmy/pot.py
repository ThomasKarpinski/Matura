pot3 = lambda x, y: x if y == 1 else 1


def pot(p, w):
    yield pot3(p, w)
    wynik = p
    for i in range(w):
        wynik *= p
    yield wynik // p


print(list(pot(int(input("podstawa: ")), int(input("wykładnik: ")))))


def pot2(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    if wykladnik == 0:
        return 1
    polowa = pot2(podstawa, wykladnik // 2)
    if wykladnik % 2 == 0:
        return polowa * polowa
    else:
        return polowa * polowa * podstawa


print(pot2(int(input("podstawa: ")), int(input("wykładnik: "))))


def pot4(p, w):
    wyn = p
    if w == 1:
        return p
    elif w == 0:
        return 1
    else:
        for i in range(w):
            wyn *= p
    return wyn // p


print(list(pot(int(input("podstawa: ")), int(input("wykładnik: ")))))

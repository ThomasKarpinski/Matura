p = int(input("Podaj podstawę: "))
w = int(input("Podaj wykładnik: "))
def pot(p, w):
    if w == 1:
        return p
    if w == 0:
        return 1
    half = pot(p, w//2)
    if w % 2 == 0:
        return half*half
    else:
        return half*half*p
print(pot(p, w))
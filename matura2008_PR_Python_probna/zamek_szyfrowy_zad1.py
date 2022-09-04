def dwojkowy(n):
    wynik = ''
    while n > 0:
        if n % 2 == 0:
            wynik += '0'
            n //= 2
        else:
            wynik += '1'
            n //= 2
    return wynik[::-1]


def zamek(n):
    b = dwojkowy(n)
    suma = 0
    for i in b:
        if i == '1':
            suma += 1
    if 2 <= len(b) <= 10 and b[1] == '0' and suma % 2 == 0:
        return True
    else:
        return False


print(zamek(766))

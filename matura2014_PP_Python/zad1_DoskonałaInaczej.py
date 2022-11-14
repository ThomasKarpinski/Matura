def doskonala(n):
    d = 2
    il = 1
    while d <= (n // 2):
        if n % d == 0:
            il *= d
        d += 1
    return "TAK" if n == il else "NIE"


print(doskonala(6))
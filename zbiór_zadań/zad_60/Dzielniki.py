with open("liczby.txt", "r") as dane:
    liczby = [int(i) for i in dane]


def dzielniki(n):
    d = 1
    l = []
    while d * d <= n:
        if d * d == n:
            l.append(d)
        if n % d == 0:
            l.append(d)
            l.append(n // d)
        d += 1
    return set(l)


"""60.1"""
mniejsze = []
for i in liczby:
    if i < 1000:
        mniejsze.append(i)
print(len(mniejsze), mniejsze[-2::])

"""60.2"""
for i in liczby:
    if len(dzielniki(i)) == 18:
        print(i)
        print(sorted(dzielniki(i)))

"""60.3"""
wzgl_pierwsze = []
for i in liczby:
    l_d = dzielniki(i)
    l_d = set(l_d)
    licznik = 0
    for j in range(1, len(liczby)):
        if len(l_d.intersection(dzielniki(j))) == 1:
            licznik += 1
    if licznik == 199:
        wzgl_pierwsze.append(i)
print(max(wzgl_pierwsze))

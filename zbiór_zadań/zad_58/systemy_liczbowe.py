files = ['dane_systemy1.txt', 'dane_systemy2.txt', 'dane_systemy3.txt']

with open(files[0]) as dane1, open(files[1]) as dane2, open(files[2]) as dane3:
    S1 = [i.split() for i in dane1]
    S2 = [i.split() for i in dane2]
    S3 = [i.split() for i in dane3]

temp1 = [int(i[1]) for i in S1]
temp2 = [int(i[1]) for i in S2]
temp3 = [int(i[1]) for i in S3]

"""58.1"""


def horner(a, p):
    h = 0
    sign = 1
    if a[0] == '-':
        sign = -1
        a = a[1:]
    for i in a:
        if ord(i) >= 65:
            h = h * p + ord(i) - 55
        else:
            h = h * p + int(i)
    return h*sign


min1 = min(temp1)
min2 = bin(horner(str(min(temp2)), 4))[3:]
min3 = bin(horner(str(min(temp3)), 8))[3:]

print(min1, '-' + min2, '-' + min3)

"""58.2"""
hour1 = [horner(i[0], 2) for i in S1]
hour2 = [horner(i[0], 4) for i in S2]
hour3 = [horner(i[0], 8) for i in S3]

licznik = 0
for h1, h2, h3 in zip(hour1, hour2, hour3):
    if h1 % 12 != 0 and h2 % 12 != 0 and h3 % 12 != 0:
        licznik += 1
print(licznik)

"""58.3"""

import math
files = ['dane_systemy1.txt', 'dane_systemy2.txt', 'dane_systemy3.txt']

with open(files[0]) as dane1, open(files[1]) as dane2, open(files[2]) as dane3:
    S1 = [i.split() for i in dane1]
    S2 = [i.split() for i in dane2]
    S3 = [i.split() for i in dane3]

temp1 = [int(i[1]) for i in S1]
temp2 = [int(i[1]) for i in S2]
temp3 = [int(i[1]) for i in S3]

"""58.1"""
min1 = min(temp1)
min2 = bin(int(str(min(temp2)), 4))[3:]
min3 = bin(int(str(min(temp3)), 8))[3:]

print(min1, '-' + min2, '-' + min3)

"""58.2"""
hour1 = [int(i[0], 2) for i in S1]
hour2 = [int(i[0], 4) for i in S2]
hour3 = [int(i[0], 8) for i in S3]

licznik = 0
for h1, h2, h3 in zip(hour1, hour2, hour3):
    if h1 % 12 != 0 and h2 % 12 != 0 and h3 % 12 != 0:
        licznik += 1
print(licznik)

"""58.3"""
maks1, maks2, maks3 = temp1[0], temp2[0], temp3[0]
licz = 1
rekord = bool
for i in range(len(temp1)):
    rekord = False
    if maks1 < temp1[i]:
        rekord = True
        maks1 = temp1[i]
    if maks2 < temp2[i]:
        rekord = True
        maks2 = temp2[i]
    if maks3 < temp3[i]:
        rekord = True
        maks3 = temp3[i]
    if rekord:
        licz += 1

print(licz)

"""58.4"""
maxi = []

for i in range(len(temp1)):
    for j in range(i + 1, len(temp1)):
        r_ij = (int(str(temp1[i]), 2) - int(str(temp1[j]), 2)) ** 2
        maxi.append(math.ceil(r_ij / abs(i - j)))
print(max(maxi))
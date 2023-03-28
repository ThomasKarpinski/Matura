with open("trojki.txt") as plik:
    trojki = [i.split() for i in plik]


# print(trojki)

def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


"""66.1"""
for trojka in range(len(trojki)):
    a = [*str(trojki[trojka][0])]
    a = sum([int(i) for i in a])

    b = [*str(trojki[trojka][1])]
    b = sum([int(i) for i in b])
    if a + b == int(trojki[trojka][2]):
        print(trojki[trojka])

"""66.2"""
for trojka in range(len(trojki)):
    if pierwsza(int(trojki[trojka][0])) and pierwsza(int(trojki[trojka][1])):
        if (int(trojki[trojka][0])) * (int(trojki[trojka][1])) == (int(trojki[trojka][2])):
            print(trojki[trojka])



"""66.3"""
def czy_prostokatny(l, i):
    if int((l[i][0])) ** 2 + int((l[i][1])) ** 2 == int((l[i][2])) ** 2:
        return True
    if int((l[i][0])) ** 2 + int((l[i][2])) ** 2 == int((l[i][1])) ** 2:
        return True
    if int((l[i][1])) ** 2 + int((l[i][2])) ** 2 == int((l[i][0])) ** 2:
        return True


for i in range(len(trojki)):
    if czy_prostokatny(trojki, i) and czy_prostokatny(trojki, i - 1):
        print(trojki[i])

"""66.4"""
def czy_trojkat(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

licznik = 0
trojkaty = 0
liczniki = []
for i in range(len(trojki)):
    if czy_trojkat(int(trojki[i][0]), int(trojki[i][1]), int(trojki[i][2])):
        licznik += 1
        trojkaty += 1
    else:
        liczniki.append(licznik)
        licznik = 0
        continue
print(max(liczniki), trojkaty)

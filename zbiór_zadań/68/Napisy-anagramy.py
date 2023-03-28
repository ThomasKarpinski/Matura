with open("dane_napisy.txt") as plik:
    napisy = [i.split() for i in plik]

"""68.1"""
licznik = 0
for i in range(len(napisy)):
    if napisy[i][0] == napisy[i][1]:
        licznik += 1
print(licznik)

"""68.2"""
def sortuj(s):
    n = len(s)
    s = list(s)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
    s = ''.join(s)
    return s


def anagramy(s1, s2):
    if len(s1) == len(s2):
        if sortuj(s1) == sortuj(s2):
            return True
        else:
            return False
    else:
        return False


counter = 0
for i in range(len(napisy)):
    if anagramy(napisy[i][0], napisy[i][1]):
        counter += 1
print(counter)

"""68.3-help"""
napisy_cal = []
for i in napisy:
    for j in i:
        napisy_cal.append(j)
# print(napisy_cal)
k_s = []
for i in range(len(napisy)):
    k = 0
    for j in range(len(napisy)):
        if napisy_cal[i] == napisy_cal[j]:
            k += 1
    k_s.append(k)
print(max(k_s))
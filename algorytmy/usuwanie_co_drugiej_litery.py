#sposób 1
def index(text):
    wynik = ""
    for i in range(len(text)):
        if i % 2 == 0:
            wynik += text[i]
    return wynik
print(index(text = input("Podaj tekst: ")))

#sposób 2
numberOfLetters = int(input("Podaj liczbę znaków wprowadzanego słowa: "))
l=[]
wyn = ""
for i in range(numberOfLetters):
    l.append(input("Litera: "))
l = l[::2]
for i in range(len(l)):
    wyn += l[i]
print(wyn)

#sposób 3
liczba = int(input("Podaj liczbę znaków wprowadzanego słowa: "))
list = []
j = 0
t = ""
while j <= (liczba - 1):
    list.append(input("Litera: "))
    j += 1
list = list[::2]
for i in range(len(list)):
    t += list[i]
print(t)

#sposób 4
k = 1
list2 = []
w = ""
number = int(input("Podaj liczbę znaków wprowadzanego słowa: "))
while (k):
    list2.append(input("Litera: "))
    k += 1
    if (k-1) == number:
        break
list2 = list2[::2]
for i in range(len(list2)):
    w += list2[i]
print(w)

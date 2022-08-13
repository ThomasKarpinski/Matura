import random


def print2d(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i][j], end=', ')


lista2D = [[1, 2, 3, 4],
           [1, 5, 7],
           [2, 9, 100]]

lista2D[1][2] = "tunczyk"

lista1D = []
lista2D.clear()

for j in range(10):
    for i in range(10):
        lista1D.append(random.randint(0, 100))
    lista2D.append(lista1D)
    lista1D = []

#print(lista2D)

tabliczka = []
rzad = []
for i in range(1, 11):
    for j in range(1, 11):
        rzad.append(i * j)
tabliczka.append(rzad)
rzad = []

#print2d(tabliczka)


listaznakow = ['x','o']

plansza = [[],
           [],
           []]
for row in range(random.randint(0, 2)):
    for col in range(random.randint(0, 2)):
        plansza.append(random.sample(listaznakow, 1))
print(plansza)
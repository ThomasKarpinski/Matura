def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

for i in gen():
    print(i)

print(list(gen()))

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 ==0:
            yield i
        i += 1
print(list(parzyste(int(input("Podaj liczbę: \n")))))

for i in parzyste(int(input("podaj liczbę: \n"))):
    print(i)
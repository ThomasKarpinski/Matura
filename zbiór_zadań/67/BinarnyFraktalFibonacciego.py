"""67.1"""
def fib(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


'''
print(fib(10))
print(fib(20))
print(fib(30))
print(fib(40))'''

"""67.2"""
def pierwsza(n):
    d = 2
    if n < 2:
        return False
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

'''
for i in range(40):
    if pierwsza(f := fib(i)):
        print(f)'''

"""67.3"""
'''
for i in range(40):
    F = bin(fib(i))[::-1]
    F = F[:-2]
    if len(bin(fib(i))[::-1]) > len(bin(fib(i + 1))[::-1]):
        print(" " + F + "\n")
    else:
        print(F + "\n")'''

"""67.4"""
for i in range(40):
    binarne = bin(fib(i))[2::]
    binarne = [*binarne]
    licznik = 0
    for j in binarne:
        if int(j) == 1:
            licznik += 1
    if licznik == 6:
        print(bin(fib(i))[2::])
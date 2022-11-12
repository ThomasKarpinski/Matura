N = 784
a = 2
b = 0
while N >= a:
    if N % a == 0:
        b += 1
        N //= a
    else:
        if b > 0:
            print(a, b)
            a += 1
            b = 0

print(a, b)

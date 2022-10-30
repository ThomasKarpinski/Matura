i = 2
n = 36
while n > 1:
    if n % i == 0:
        n //= i
        print(i)
    else:
        i += 1

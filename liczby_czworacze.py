n = 200000
primes = []
notPrimes = []
temp = [True] * (n + 1)
for i in range(2, n):
    if temp[i]:
        primes.append(True)
        for j in range(i * i, n + 1, i):  # usuwanie wielokrotności liczb
            temp[j] = False
            notPrimes.append(False)
print(primes)
print(notPrimes)

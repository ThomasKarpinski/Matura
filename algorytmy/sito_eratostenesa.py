def sito_eratostenesa(n):
    primes = []
    temp = [True] * (n + 1)
    for i in range(2, n):
        if temp[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):  # usuwanie wielokrotności liczb
                temp[j] = False
    return primes


print(sito_eratostenesa(int(input("Podaj zakres: "))))

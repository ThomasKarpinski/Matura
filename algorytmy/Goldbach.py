"""algorytm zoptymalizowany przy użyciu sita eratostenesa"""


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


def find_goldbach(n):
    if n <= 2 or n % 2 == 1:
        print("Podaj parzystą liczbę większą od 2")
        return
    primes = sieve_of_eratosthenes(n)
    for p in primes:
        if n - p in primes:
            return p, n - p
    return None


"""algorytm nieoptymalny"""


def find_goldbach_no(n):
    if n <= 2 or n % 2 == 1:
        print("Podaj parzystą liczbę większą od 2")
        return
    primes = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    for p in primes:
        if n - p in primes:
            return p, n - p
    return None
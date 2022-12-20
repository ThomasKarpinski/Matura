def sito_eratostenesa(n):
    primes = []
    temp = [True] * (n + 1)
    for i in range(2, n):
        if temp[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                temp[j] = False
    return primes


def prime_number(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def odd_primes(N):
    oddprimes = sito_eratostenesa(N)
    oddprimes.remove(2)
    return oddprimes


with open("liczby.txt") as plik:
    liczby = [int(i) for i in plik]

    """3.2"""
    licznik = 0
    for i in liczby:
        if prime_number(i - 1):
            licznik += 1
    print(licznik)

    """3.3"""
    rozklady = []
    for i in liczby:
        rozklady.append(sito_eratostenesa(i))
    # print(rozklady)

    zestawienie = list(zip(liczby, rozklady))
    # print(zestawienie)

    """3.4"""
    szes = []
    for i in liczby:
        szes.append(hex(i)[2::])
    szes = ",".join(szes)

    for i in range(0, 16):
        print(f"{hex(i)[2::]}:{szes.count(hex(i)[2::])}")

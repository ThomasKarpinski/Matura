with open("ciagi.txt", "r") as plik:
    sequences = [i.strip() for i in plik]

    """1"""
    for number in sequences:
        if (dl := len(number)) % 2 == 0:
            half = dl // 2
            if number[:half] == number[half:]:
                print(number)

    """2"""
    counter = 0
    for number in sequences:
        if '11' not in number:
            counter += 1
    print(counter)

    """3"""
    def isPrime(n):
        d = 2
        if n < 2:
            return False
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True


    def hasPrimeDividers(number):
        # Liczby pierwsze zaczynają się od 2
        for divider in range(2, number + 1):  # rób tak długo, aż dzielnik będzie równy liczbie
            if isPrime(divider):  # rób tylko wtedy, gdy jeden z dzielników jest liczbą pierwszą
                if number % divider == 0:
                    # sprawdzić drugi rozdzielacz
                    if isPrime(number / divider):  # liczba dzielona musi być również pierwsza
                        return True
                    else:
                        # drugi dzielnik nie jest pierwszy
                        return False
        return False


    def semiPrimeNumbers():
        semiPrimes = []
        decValues = [int(x, 2) for x in sequences]  # z bitów na dziesiętne
        for number in decValues:  # rób dla każdej liczby
            if number > 1:  # 1 nie może być półpierwszą
                if (hasPrimeDividers(number)):
                    semiPrimes.append(number)

        print("min = " + str(min(semiPrimes)))
        print("max = " + str(max(semiPrimes)))

        return len(semiPrimes)


    print("Jest " + str(semiPrimeNumbers()) + " liczb polpierwszych")

'''Program sprawdza czy liczba jest liczbą pierwszą.'''

def prime_number(number):

    counter = 0
    for i in range(1,number+1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        return f"{number} is prime number."
    else:
        return f"{number} isn't prime number."

print(prime_number(int(input("Please, enter the number to check if it's a prime number: "))))
from random import randint

'''print("Welcome to the game called 'guess what number it is'\n"
      "If you will get bored, just write 'exit'.")'''


def guessing_the_number():

    computer_number = randint(1, 9)
    player_number = -1
    counter = 0

    while True:
        while player_number != computer_number:
            counter += 1
            player_number = int(input("Enter your number: "))
            if computer_number > player_number:
                print("Your number is less than required.")
            elif computer_number < player_number:
                print("Your number is greater than the required number")
            else:
                print(f"{computer_number} is required number")
                print(f"Gratulations! You guessed after {counter} times\n"
                      "Are you still playing?")
        decision = input("'exit' or 'next': ")
        if decision == "exit":
            break
        else:
            return guessing_the_number()


#  guessing_the_number()

def reversig_order_words():

    sequence = []
    for i in range(1, 11):
        sequence.append(input("Podaj wyraz: "))
    reversed_sequence = sequence[::-1]
    result = ""
    for j in range(len(reversed_sequence)):
        result += reversed_sequence[j] + " "
    print(result)


reversig_order_words()

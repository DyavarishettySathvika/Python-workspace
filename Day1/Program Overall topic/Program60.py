import random

number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("Correct Guess!")
else:
    print("Wrong! Number was", number)
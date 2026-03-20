import random

num = random.randint(1, 50)
guess = 0

while guess != num:
    guess = int(input("Guess a number (1-50): "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")

print("Correct! The number was", num)
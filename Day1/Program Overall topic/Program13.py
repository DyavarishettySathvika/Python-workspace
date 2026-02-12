# 5. Guess a number game
import random

secret = random.randint(1, 10)  # Pick a random number
print("Guess a number between 1 and 10")

for tries in range(3):          # Give 3 tries
    guess = int(input("Your guess: "))
    if guess == secret:
        print("You guessed it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Sorry, the number was", secret)

print("Game over!")
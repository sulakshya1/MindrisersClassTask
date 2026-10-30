
import random

print("=" * 35)
print("      NUMBER GUESSING GAME")
print("=" * 35)

# Generates a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            attempts -= 1

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print("\nCongratulations! You guessed the number!")
            print(f"The secret number was {secret_number}.")
            print(f"Total attempts: {attempts}")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")

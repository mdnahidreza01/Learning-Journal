import random

secret_number = random.randint(1, 100)
attempts = 0

print(">>> NUMBER GUESSING GAME <<<")
print("Hi there! I'm thinking of a number from 1 to 100. Now, guess the number")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > 100 or guess < 1:
            print("The number is between 1 and 100. Try again")
        elif guess < secret_number:
            print("The Number is Too low! Try again.")

        elif guess > secret_number:
            print("The Number is Too high! Try again.")

        else:
            print(f"Correct! You won in {attempts} attempts!")
            break

    except ValueError:
        print("Please enter a valid whole number.")

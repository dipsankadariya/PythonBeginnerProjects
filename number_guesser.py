import random

def guess_number():
    number = random.randint(1, 100)  
    tries = 0

    print("Guess the number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))

        tries += 1

        if guess < number:
            print("low! Try again.")
        elif guess > number:
            print(" high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {tries} tries.")
            break

guess_number()
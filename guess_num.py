import random

def generate_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def give_hint(number, guess, previous_guesses):
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

    if len(previous_guesses) > 1:
        difference = abs(number - guess)
        if difference <= 5:
            print("You're very close!")
        elif difference <= 10:
            print("You're close!")

def play_game():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number. I'll give you hints along the way.")

    number = generate_number()
    attempts = 0
    previous_guesses = []

    while True:
        guess = get_user_guess()
        attempts += 1
        previous_guesses.append(guess)

        if guess == number:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
        else:
            give_hint(number, guess, previous_guesses)

play_game()

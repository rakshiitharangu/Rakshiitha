import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = input("Enter your guess: ")
        
        try:
            guess = int(guess)
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

number_guessing_game()
import random

def number_guessing_game():
    # Game configuration
    LOWER_BOUND = 1
    UPPER_BOUND = 100
    MAX_ATTEMPTS = 10
    
    # Generate random number
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it!\n")
    
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! 📉 Try again.")
        else:
            print("Too high! 📈 Try again.")
        
        # Show remaining attempts
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")
    
    else:
        print(f"\n💔 Game Over! The number was {secret_number}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()

import random

def play_game():
    while True:
        # Generate a new secret number at the start of each round
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print("\n--- New Round ---")
        print("A new secret number between 1 and 100 has been chosen.")

        # Guessing loop for the current round
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the secret number ({secret_number}) in {attempts} attempts.")
                break

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

# Run the game
play_game()

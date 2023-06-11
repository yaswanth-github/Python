import random

def play_game():
    # generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        # get user's guess
        user_guess = input("Guess a number between 1 and 100: ")
        
        # convert user's guess to an integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        num_guesses += 1
        
        # check if the user's guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} tries.")
            break
        else:
            # give a hint to the user
            if user_guess < secret_number:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()

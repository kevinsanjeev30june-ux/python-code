# Rock , Paper, Scissors Game
import random

while True:
    user_actions = input("Enter rock, paper, or scissors):")
    possible_actions = ["rock", "paper", "scissors"]

    # using random function
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_actions}, computer chose {computer_action}.\n")

# Condition for checking the winner
    if user_actions == computer_action:
        print(f"Both players selected {user_actions}. It's a tie!")
    elif user_actions == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_actions == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_actions == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

# Take input for playing again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
import random
computer_guess = random.randint(1, 10)

while True:
 user_guess = int(input("Guess a number between 1 and 10: "))

 if user_guess == computer_guess:
    print("Congratulations! You guessed the number correctly.")
 else:
    print("You loose!! Better luck next time.")
# Number Guessing game 
import random

num = random.randint(1,50)
lives = 5 
print("Number Guessing Game")

while lives > 0 :
    guess = int(input("Enter a number :"))

    if guess == num :
        print("You won the game")
        break

    else:
        print("You lost the game")
        
Lives = lives- 1
print("Lives:", lives)

print("Number was:", num )
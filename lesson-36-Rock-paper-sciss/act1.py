import tkinter as tk
from tkinter import  messagebox
import random

# Create a main window
root = tk.Tk()
root.title("Length Converter App")   # As requested
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\n"
             f"Computer's Choice: {computer_choice}\n\n"
             f"{result}"
    )


# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
heading.pack(pady=20)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=30, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=30, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=30, command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 25), justify="center")
result_label.pack(pady=30)

# Run application
root.mainloop()

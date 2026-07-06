from tkinter import *
from datetime import date
from unittest import result

# function to calculate age
def calculate_age():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    age = today.year - year

    # Check if birthday has occurred this year  
    if (today.month, today.day) < (month, day):
        age -= 1

    result.config(text=f"{name}, you are {age} years old.")

# Create the main window
root = Tk()
root.title("Age Calculator")
root.geometry("400x300")

# Create labels and entry 
Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Enter your Date").grid(row=1, column=0)
day_entry = Entry(root)
day_entry.grid(row=1, column=1)

Label(root, text="Enter your Month").grid(row=2, column=0)
month_entry = Entry(root)
month_entry.grid(row=2, column=1)

Label(root, text="Enter your Year").grid(row=3, column=0)
year_entry = Entry(root)
year_entry.grid(row=3, column=1)

# Create a button to calculate age
button = Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=0, columnspan=2, pady=10)

# result label to display the age
result = Label(root, text="")
result.grid(row=5, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
# import necessary libraries
from tkinter import *
from datetime import date

# create a window
root = Tk()
root.title("Getting started with widget")
root.geometry("400x300")

# add widgets 
# add a label
lbl = Label(text="Hello, Tkinter!", fg="blue", bg="#072F5F", height=2, width=300)

# ADD LABEL FOR GETTING NAME AS INPUT FROM USER
# Use ENTRY WIDGET TO CREATE A TEXT BOX FOR USER TO ENTER DETAILS
name_lbl = Label(text="Full Name:",  bg="#3895D3",) 
name_entry = Entry()

# Function to display a message
def display():
    # Read the input given by the user
    name = name_entry.get()
    # Declaring a global variable
    # to make it acessible anywhere in the program
    global message
    message = "Welcome to the application tkinter! \nToday's date is: "
    greet = "Hello "+ name + "\n"
    # Display the details in the text box
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

    # Add a text widget to display the message
    text_box = Text(height=3)

    # Add a button and give value of command as name of the function 
    # Press the button display function will be called automatically
    btn = Button(text="Begin", command=display, height=2, bg="#072F5F", fg="white")

    # Organize the widgets in the window
    lbl.pack()
    name_lbl.pack()
    name_entry.pack()
    btn.pack()
    text_box.pack()

    # start the Gui event loop
    root.mainloop()
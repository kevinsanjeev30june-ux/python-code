# Import neceessary libraries
from tkinter import *

# Create a window
root = Tk()
root.title("LOGIN APP")
root.geometry("400x400")

# Create a frame to organize elements better
frame = Frame(master=root, height=500, width=400 bg='#01124e')

# add widgets
# add a label
lbl1 = Label(frame, text="Full Name", bg='#f99d38', fg='white',width=20, )
lbl2 = Label(frame, text="Email ID", bg='#f99d38', fg='white',width=20)
lbl3 = Label(frame, text="Password", bg='#f99d38', fg='white',width=20)

# Use entry widget to create text boxes for user to enter data
name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show='*')

# Function to display the message
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations! You have successfully logged in."
    text_box.insert(END, greet)
    text_box.insert(END, message)

# Text box to display the message    
text_box = Text(bg='#de004b' , fg='blue')


# Import neceessary libraries
from tkinter import *

# Create a window
root = Tk()
root.title("LOGIN APP")
root.geometry("400x400")

# Create a frame to organize elements better
frame = Frame(master=root, height=500, width=400 ,bg='#01124e')

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

# Add a button ,when pressed the message will be displayed
btn = Button(text="create account", command=display , bg="red")

# Arrange all the widgets 
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=150, y=200)
text_box.place(y=250)

# start the main loop
root.mainloop()
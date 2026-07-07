# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Message Box Example")
root.geometry("400x300")

# Function for displaying warning message
# This will be called when the button is clicked
# messagebox.showwarning() ("Window Title", "Text to display in the message box"
def msg():
    # messagebox.showwarning("Alert", "STOP! Virus found.")
    messagebox.showinfo("Alert", "STOP! Virus found.")
    # messagebox.showerror("Alert", "STOP! Virus found.")

# Adding Button widget to the main window    
button = Button(root, text="Scan for Virus", command=msg)
button.pack(pady=40)

# Start the main event loop
root.mainloop()
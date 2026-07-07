# Import necessary libraries
from tkinter import*

# Create the main window
root = Tk()
root.title("Event Handler")
root.geometry("400x300")

# Event handler for key press
def handle_keypress(event):
    """Print the character associated with the key pressed."""
    print(event.char)


# Bind the keypress event to the handle_keypress ()
root.bind("<KeyPress>", handle_keypress)

# Event handler for button click
def handle_click_left(event):
    print("\nThe button was LEFT clicked!")

def handle_click_right(event):    
    print("\nThe button was RIGHT clicked!")

def handle_click_scroll(event):
    print("\nThe button was SCROLLED!")    

button = Button(root, text="Click Me!")    
button.pack()

# Bind click event to the handle_click()
button.bind("<Button-1>", handle_click_left)  
button.bind("<Button-2>", handle_click_scroll)
button.bind("<Button-3>", handle_click_right)

# Start the main event loop
root.mainloop()
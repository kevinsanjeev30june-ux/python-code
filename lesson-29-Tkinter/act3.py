from tkinter import *

# function to  calculate product
def product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    text_box.delete("1.0", END)
    text_box.insert(END, f"Product: {num1 * num2}")

#  Create a main window
root = Tk()
root.title("Product Calculator")
root.geometry("700x600")

# Create labels
label1 = Label(root, text="Enter two numbers to calculate their product:")
Label(root, text="Number 1:")
entry1 = Entry(root)
Label(root, text="Number 2:")
entry2 = Entry(root)

# Create a button 
btn = Button(root, text="Calculate Product", command=product)

# Create a text widget to display the result
text_box = Text(root, height=5, width=50)

# Organize the widgets in the window
label1.pack()
Label(root, text="Number 1:").pack()
entry1.pack()
Label(root, text="Number 2:").pack()
entry2.pack()
btn.pack()
text_box.pack()

root.mainloop()
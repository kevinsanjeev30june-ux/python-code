# Import necessary libraries
from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename

# Create the main window
root = Tk()
root.title("Simple Text Editor")
root.geometry("600x400")
root.rowconfigure(0, minsize=600, weight=1)
root.columnconfigure(1, minsize=600, weight=1)

# Function to open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    # If a file is opened then display the contents of the file
    with open(filepath, "r") as input_file:
        # Read contents of the input file
        text = input_file.read()
        # Insert the contents of the file in editor box
        txt_edit.insert(END, text)
        input_file.close()
    root.title(f"Simple Text Editor - {filepath}")    

# Function to save a file
def save_file():
     # Save the current file as a new file.
     filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
     if not filepath:
        return
     with open(filepath, "w") as output_file:
         # Read the edited content and update in the output life
         text = txt_edit.get(1.0, END)
         output_file.write(text)
     root.title(f"Simple Text Editor - {filepath}")

# ADD widgets in the application
txt_edit = Text(root)         
fr_buttons = Frame(root, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# start the main event loop
root.mainloop()
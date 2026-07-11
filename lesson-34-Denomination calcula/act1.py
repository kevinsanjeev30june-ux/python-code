from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up the main window
root = Tk()
root.title("Denomination Calculator")
root.configure(bg="Dark blue")
root.geometry("600x400")

# Adding image and labels in main window
upload = Image.open("Calc.png")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image= image , bg = "Dark blue")
label.place(x = 180 , y = 20)

label1 = Label(
    root,
    text ='Hey User! Welcome to denomination counter Application.',
    bg= "Dark blue"
)
label1.place(relx=0.5, y = 340 , anchor=CENTER)

#  Function to open messages
def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?")
    
    if MsgBox == "ok":
        topwin()

# ADDING BUTTON IN MAIN WINDOW
button1 = Button(
    root,
    text= "Let's get started!",
    command=msg,
    bg= 'Brown',
    fg = 'White'
)        
button1.place(x= 260 , y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations calculator")
    top.configure(bg = 'Red')
    top.geometry("600*350+50+50")

    label =Label(top , text ="Enter total amount" , bg ="red")
    entry = Entry(top)

    lbl = Label(
        top,
        text ="Here are number of notes for each denomination",
        bg = "Red"
    )
    l1 = Label(top , text ="2000 ", bg="Red")
    l2 = Label(top , text ="500 ", bg="Red")
    l3 = Label(top , text ="100", bg="Red")
    
    t1 = Entry(top)
    t2 = Entry(top)
    t3= Entry(top)
    
# Calculation function
def calculator():
    try:
        amount = int(Entry.get())
        
        note2000 = amount // 2000
        amount %= 2000

        note500 = amount // 500
        amount %= 500

        note100 = amount // 100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))

    except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
         top,
        text="Calculate",
        command=calculator,
        bg="Brown",
        fg = "White")
    
# Placing Widgets
label.place(x=230, y=50)
Entry.place(x=260, y=360)
Button.place(x=240, y=120)

label.place(x=140, y=170)
    
label1.place(x=180, y=200)
lbl2.place(x=180, y=230)
label3.place(x=180, y=260)

t1.place(x=270, y=200)
t2.place(x=270, y=230)
t3.place(x=270, y=260)

top.mainloop()


# Start main loop
root.mainloop()

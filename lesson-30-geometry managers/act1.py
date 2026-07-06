from tkinter import*

# Crearte a window
root = Tk()
root.title("NUMBER PAD")
root.geometry("400x400")

nums = [[9,8,7],[6,5,4],[3,2,1],['#','0','=']]
#border_effect = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=75)
    for j in range(0, 3):
        frame = Frame(master=root, relief=RAISED, borderwidth=8)
        frame.grid(row=i, column=j)

        label = Label(master=frame, text=nums[i][j], bg="#785b8b", fg="white")
        label.pack(padx=3, pady=3)

root.mainloop()        
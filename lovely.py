
import tkinter.messagebox as mb
from tkinter import *
import random
def show():
    mb.showinfo("Haha", "Knew it")
    root.destroy()
def move_btn(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)
root = Tk()
root.geometry("400x400")
question_label = Label(root, text="Are you idiot ?")
question_label.pack(pady=20)
yes_button = Button(root, text="Yes", command=show)
yes_button.pack()
no_button = Button(root, text="No")
no_button.pack()
no_button.bind("<Enter>", move_btn)
root.mainloop()
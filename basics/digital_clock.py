from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root,font=("Helvetica", 100), background = "black", foreground = "cyan")
label.pack(anchor = CENTER)
time()

mainloop()
    


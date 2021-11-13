from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("digital-7", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
# Credits: Coding with evan - Youtube
# Fonts: https://www.1001fonts.com/digital-7-font.html

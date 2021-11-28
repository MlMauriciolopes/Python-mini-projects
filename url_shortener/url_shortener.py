import pyperclip # pip install pyperclip
import pyshorteners # pip install pyshortteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url = StringVar()
url_addrerss = StringVar()

def urlshortener():
    urladrerss = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladrerss)
    url_addrerss.set(url_short)

def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)

Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_addrerss).pack(pady=5)
Button(root, text="Copy URL", command= copyurl).pack(pady=5)

root.mainloop()



# Credits: Coding with Evan - Youtube
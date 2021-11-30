#
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image # pip instlall pillow
from googletrans import Translator # pip install googletrans==3.1.0a0
from tkinter import messagebox

root = Tk()
root.title('langauge Translator')
root.geometry('530x330')
root.resizable(False, False)
root.config(bg='#6495ED')
#root.iconbitmap('translate.ico') # this is for set app icon

# function for translate the language and set in 12 box
def translate():
    langauge_1 = t1.get("1.0", "end-1c")
    c1 = choose_langauge.get()

    if langauge_1 == '':
        messagebox.showerror('Language Translator', 'please fill the box')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(langauge_1, dest=c1)
        t2.insert('end', output.text)

#for clear the both t1 and t2 box
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

img = ImageTk.PhotoImage(Image.open('translate.png'))
label = Label(image=img, bg='#6495ED')
label.place(x=230, y=3)

a = StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'))

auto_detect['values'] = ('Auto Detect', )

auto_detect.place(x=30, y=70)
auto_detect.current(0)

t1 = StringVar()
choose_langauge['values'] = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani',
    'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 
    'Cebuano', 'Chichewa'
)

choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
                command=translate, bg= '#323233', fg='#fff')
button.place(x=150, y=280)

clear = Button(root, text="Clear", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
                command=clear, bg= '#323233', fg='#fff')
button.place(x=280, y=280)

root.mainloop()

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
                command=translate, bg= '#323233' , fg='fff')
button.place(x=150, y=280)

clear = Button(root, text="Clear", width=10, font=('verdana', 10, 'bold'), cursor="hand2",
                command=clear, bg= '#323233' , fg='fff')
clear.place(x=280, y=280)

root.mainloop()


# Credits: _python.py_ - Instagram


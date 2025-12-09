# Farah Mahmoud section 4
from tkinter import *
import webbrowser

root = Tk()

root.geometry('500x400')
root.title('Home')

def fun():
    webbrowser.open(r'https://youtu.be/BnquzIGVuKc?si=Mh9Lxh7Qh-Wab8Jk')

btn = Button(root, command=fun, text='click me', width='12', height='3', fg='white', bg='black', font='25')
btn.pack()

root.mainloop()

import Colleges.Les12.LoginFrame
from tkinter import *

def toonLoginFrame():
    hoofdframe.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()

def login():
    if loginfield.get() == "admin":
        toonHoofdFrame()
    else:
        print('Verkeerde gebruikersnaam!')


root = Tk()

loginframe, loginfield = Colleges.Les12.LoginFrame.creeerLoginFrame(root, login)

hoofdframe = Label(master=root,
 text='Hello World',
 background='white',
 foreground='blue',
 font=('Helvetica', 16, 'bold italic'),
 width=20,
 height=3)

hoofdframe.pack()


hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

toonLoginFrame()
root.mainloop()


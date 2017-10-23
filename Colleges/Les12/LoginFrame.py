from tkinter import *

def creeerLoginFrame(rootParam, loginFunc):
    loginframe = Frame(master=rootParam)
    loginframe.pack(fill="both", expand=True)
    loginfield = Entry(master=loginframe)
    loginfield.pack(padx=20, pady=20)
    loginbutton = Button(master=loginframe, text='login', command=loginFunc)
    loginbutton.pack(padx=20, pady=20)

    return (loginframe, loginfield)
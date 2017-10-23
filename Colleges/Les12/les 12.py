from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()

label = Label(master=root,
 text='Hello World',
 background='white',
 foreground='blue',
 font=('Helvetica', 16, 'bold italic'),
 width=20,
 height=3)

label.pack()


def hallo():
 grondtal = int(entry.get())
 kwadraat = grondtal ** 2
 tekst = "kwadraat: van {} = {}"
 label["text"] = tekst.format(grondtal, kwadraat)

def clicked():
 bericht = 'Chris je moeder!'
 showinfo(title='popup', message=bericht)



button1 = Button(master=root, text='Button 1',command=hallo)
button1.place(x=10, y=100)

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)


entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()

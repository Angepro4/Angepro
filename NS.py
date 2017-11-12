from tkinter import *
from langs import teksten
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from vertrekXML import *
import requests
import xmltodict
import time


aantalkliks = 0
bestemmingen = list()
testz = list()
testz1 = list()
aantalkliks1 = 0
weg = []


def update_timeText(): # Functie voor tijd linksonder
    current = time.strftime("%H:%M:%S")
    timeText.configure(text=current)
    root.after(1000, update_timeText)

def maakbuttons(): # Eerste rij van toetsenbord
    global weg
    count = 0
    lst = []
    for letter in 'ABCDEFGHI':
        Buttons = Button(master=root, text=letter, height=2, width=8, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda x=letter: set_text(x))
        Buttons.place(x=223+100*count, y=540)
        Buttons.configure(font=("Courier", 13, 'bold'))
        count+=1
        weg.append(Buttons)

def maakbuttons1(): # Tweede rij van toetsenbord
    global web
    count = 0

    for letter in 'JKLMNOPQRST':
        Buttons = Button(master=root, text=letter, height=2, width=8, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda x=letter: set_text(x))
        Buttons.place(x=223+100*count, y=620)
        Buttons.configure(font=("Courier", 13, 'bold'))
        weg.append(Buttons)
        count+=1

def maakbuttons2(): # Derde rij van toetsenbord
    global web
    count = 0
    for letter in 'UVW':
        Buttons = Button(master=root, text=letter, height=2, width=8, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda x=letter: set_text(x))
        Buttons.place(x=223+100*count, y=700)
        Buttons.configure(font=("Courier", 13, 'bold'))
        weg.append(Buttons)
        count+=1

def maakbuttons3(): # Toetsenbord spatie
    global weg
    count = 0
    for letter in ' ':
        Buttons = Button(master=root, height=2, width=48, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda x=letter: set_text(x))
        Buttons['text'] = teksten['toetsenbord'][taal]
        Buttons.place(x=523, y=700)
        Buttons.configure(font=("Courier", 13, 'bold'))
        weg.append(Buttons)
        count+=1

def maakbuttons4(): # Derde rij toetsenbord
    count = 0
    global weg
    for letter in 'XYZ':
        Buttons = Button(master=root, text=letter, height=2, width=8, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda x=letter: set_text(x))
        Buttons.place(x=1023+100*count, y=700)
        Buttons.configure(font=("Courier", 13, 'bold'))
        count+=1
        weg.append(Buttons)

def set_text(text):  # Functie om letter toe te voegen zodra er op knop van toeteenbord wordt geklikt
    a = entry.get() + text
    entry.delete(0, len(entry.get()))
    entry.insert(0, a)

def remove_letter(): # Functie voor de backspace om ingevoerde letter te verwijderen
    last = len(entry.get())-1
    if last >= 0:
        entry.delete(last)


def keyboardadd(): # Voeg keyboard toe voor buttons die toetsenbord moeten aanroepen
    maakbuttons()
    maakbuttons1()
    maakbuttons2()
    maakbuttons3()
    maakbuttons4()
    backspace.place(x=1123, y=540)


def removekeyboard(): # Haal keyboard weg voor buttons die toetsenbord weg moeten halen
    backspace.place_forget()
    for button in weg:
        button.place_forget()



def maakEntryLeeg(): # Maak invul balkje leeg voor bv opnieuw zoeken
    entry.delete(0, END)
    entry.insert(0, "")


def zelfInvullen():  # Haalt uit de API gegevens op voor de button Andere locaties
    lst = []
    try:
        errorlabel.place_forget()
        auth_details = ('yassine.benhadi@student.hu.nl', 'B9MtIu7EkzS9Jd14pOqTtwy3lBUlxlE0bbrCk-hHduGhOk3MSBCd9g')
        deel_url = 'http://webservices.ns.nl/ns-api-avt?station='
        deel_url2 = entry.get()
        api_url = deel_url + str(deel_url2)
        response = requests.get(api_url, auth=auth_details)
        vertrekXML = xmltodict.parse(response.text)
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            if 'VertrekVertragingTekst' in vertrek.keys():
                vertraging = vertrek['VertrekVertragingTekst'][0:2]
            else:
                vertraging = ''
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            spoor = vertrek['VertrekSpoor']
            lst.append('{:<5}{:2} {:<23}  {:>3}'.format(vertrektijd, vertraging, eindbestemming, spoor['#text']))
    except KeyError: # Bij foute invoer entry :

        button6['text'] = teksten['button6'][taal]
        button6.place(x=1100, y=80)
        button9.place_forget()
        button8.place_forget()
        keyboardadd()
        maakEntryLeeg()
        Perron.place_forget()
        actueelTitel.place_forget()
        for label in testz:
            label.place_forget()
        errorlabel['text']=teksten['noLocation'][taal]

        errorlabel.place(x=600,y=300)
    return lst


def zelfInvullen1(): # Voor button Andere locaties
    button9['text'] = teksten['button9'][taal]
    button9.place(x=1100, y=80)
    global aantalkliks1
    aantalkliks1 = 0
    removekeyboard()
    actueelTitel['text'] = teksten['actueelTitelLoc'][taal]
    actueelTitel.place(x=560, y=110)
    Perron['text'] = teksten['labelperron'][taal]
    Perron.place(x=1090, y=160)
    errorlabel.place_forget()
    global testz
    global bestemmingen
    bestemmingen = zelfInvullen()


    if aantalkliks * 8 < len(bestemmingen):
        geef_labels(0)
        button7['text'] = teksten['button7'][taal]
        button7.place(x=975, y=680)
    else:
        button7.place_forget()


def geef_labels(richting): # Voor button Andere locaties. Hier worden alle labels gemaakt en verschijnt de volgende en/of vorige button.

    global aantalkliks1
    aantalkliks1=0
    count = 0
    global aantalkliks
    global testz
    aantalkliks += richting
    if len(testz) > 0:
        for label in testz:
            label.place_forget()
    for stad in bestemmingen[(aantalkliks*8):8+(aantalkliks*8)]:
        label = Label(master=root, foreground='white', background='#03328F', justify=LEFT, padx=20, pady=5)
        label.config(font=("Courier", 20, 'bold'))
        label.place(x=560, y=190 + 60 * count)
        label["text"] = stad
        testz.append(label)
        count += 1
    aantalkliks+=1
    if aantalkliks == 1:
        button8.place_forget()
    else:
        button8['text'] = teksten['button8'][taal]
        button8.place(x=560, y=680)
    if aantalkliks*8 > len(bestemmingen):
        button7.place_forget()
    else:
        button7['text'] = teksten['button7'][taal]
        button7.place(x=975, y=680)

def vertrek(): # Hier worden de gegevens uit de API aangeroepen voor de station Utrecht. Functie is geschreven voor button Huidige locatie
    global aantalkliks1
    aantalkliks1 = 0
    button8.place_forget()
    removekeyboard()
    sluitoverigelocaties()
    Perron['text'] = teksten['labelperron'][taal]
    Perron.place(x=1090, y=116)
    actueelTitel['text'] = teksten['actueelTitelLoc'][taal]
    actueelTitel.place(x=570, y=50)
    global testz1
    global bestemmingen
    bestemmingen = vertrekTijden()

    if aantalkliks1 * 8 < len(bestemmingen):
        geef_labels1(0)
        button10['text'] = teksten['button10'][taal]
        button10.place(x=980, y=680)
    else:
        button10.place_forget()

def geef_labels1(richting): # Voor button Huidige locaties. Hier worden alle labels gemaakt en verschijnt de volgende en/of vorige button.
    global aantalkliks
    aantalkliks = 0
    count = 0
    global aantalkliks1
    aantalkliks = 1
    global testz1
    aantalkliks1 += richting
    if len(testz) > 0:
        for label in testz:
            label.place_forget()
    for stad in bestemmingen[(aantalkliks1 * 8):8 + (aantalkliks1 * 8)]:
        label = Label(master=root, foreground='white', background='#03328F', justify=LEFT, padx=20, pady=5)
        label.config(font=("Courier", 20, 'bold'))

        label.place(x=560, y=150 + 60 * count)
        label["text"] = stad
        testz.append(label)
        count += 1
    aantalkliks1 += 1

    if aantalkliks1 == 1:
        button11.place_forget()
    else:
        button11['text'] = teksten['button11'][taal]
        button11.place(x=558, y=680)
    if aantalkliks1*9 > len(bestemmingen):
        button10.place_forget()
    else:
        button10['text'] = teksten['button10'][taal]
        button10.place(x=980, y=680)




def error(): # Voor de eerste twee buttons een popup
    bericht = 'Deze functie is uitgeschakeld.'
    showinfo(title='popup', message=bericht)


def toonHoofdFrame(): # Functie toont hoofdmenu aan, de ga terug naar het hoofdmenu button maakt hier gebruik van ook begint het programma hiermee.
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global backbutton2
    global panel
    global buttonlanguageNL
    global buttonlanguage
    global aantalkliks
    aantalkliks = 0
    global aantalkliks1
    aantalkliks1 = 0
    button8.place_forget()
    removekeyboard()
    sluitoverigelocaties()

    Perron.place_forget()
    actueelTitel.place_forget()

    if taal == 'nl':
        panel.place(x=540, y=100)
    elif taal == 'en':
        panelA.place(x=540, y=100)
    backbutton2.place_forget()
    button4.place_forget()
    button5.place_forget()
    button1['text'] = teksten['button1'][taal]
    button1.place(x=380, y=540)
    button2['text'] = teksten['button2'][taal]
    button2.place(x=670, y=540)
    button3['text'] = teksten['button3'][taal]
    button3.place(x=960, y=540)
    buttonlanguage.place(x=210, y=25)
    buttonlanguageNL.place(x=320, y=25)

def toonTweedeFrame(): # Toon tweede frame gemaakt voor button reisinformatie.
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global backbutton2
    global panel
    global buttonlanguageNL
    global buttonlanguage
    removekeyboard()
    sluitoverigelocaties()
    buttonlanguageNL.place_forget()
    buttonlanguage.place_forget()
    panelA.place_forget()
    panel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4['text'] = teksten['button4'][taal]
    button4.place(x=210, y=70)
    button5['text'] = teksten['button5'][taal]
    button5.place(x=210, y=170)
    backbutton2['text'] = teksten['backbutton2'][taal]
    backbutton2.place(x=210, y=270)


def overigeLocaties(): # Functie wordt aangeroepen door button Andere locaties (toont keyboard etc)
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global backbutton2
    global panel
    global buttonlanguageNL
    global buttonlanguage
    for label in testz:
        label.place_forget()
    keyboardadd()


    Perron.place_forget()
    actueelTitel.place_forget()


def sluitoverigelocaties(): # Sluit Andere locaties zodra van scherm moet worden gewisseld. Huidige locatie maakt hier gebruik van.
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global backbutton2
    global panel
    global buttonlanguageNL
    global buttonlanguage
    button10.place_forget()
    button11.place_forget()
    button9.place_forget()
    button8.place_forget()
    button7.place_forget()
    maakEntryLeeg()
    errorlabel.place_forget()
    entry.place_forget()
    button6.place_forget()
    for label in testz:
        label.place_forget()

def overigeLocaties1(): # De button ZOEK roept deze functie aan. Hier worden weer gegevens opgeroepen uit functie overigeLocaties
    button10.place_forget()
    button11.place_forget()
    global aantalkliks
    aantalkliks = 0
    button8.place_forget()
    button7.place_forget()
    button9.place_forget()
    global aantalkliks1
    aantalkliks1 = 0
    maakEntryLeeg()
    errorlabel.place_forget()
    button6['text'] = teksten['button6'][taal]
    button6.place(x=1100, y=80)
    entry.place(x=560, y=79)
    overigeLocaties()

taal = 'nl'
def clickedEN(): # Overschakelen naar het Engels
    global taal
    taal='en'
    toonHoofdFrame()
    panel.place_forget()
    panelA.place(x=540, y=100)

def clickedNL(): # Overschakelen naar het Nederlands
    global taal
    taal='nl'
    toonHoofdFrame()
    panelA.place_forget()
    panel.place(x=540, y=100)


# Start GUI
root = Tk()
a = root.wm_attributes('-fullscreen', 1)



C = Canvas(root, bg="blue", height=250, width=300) # Achtergrond
filename = ImageTk.PhotoImage(file="images\\leeg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


timeText = Label(root, text="", background='#FECE22', font=("Helvetica", 20)) # Label voor tijdstip links onder
timeText.place(x=200, y=780)
update_timeText()

actueelTitel = Label(master=root, foreground='#03328F', height=2, background='#FECE22') # Label Actuele vertrektijden:
actueelTitel.configure(font=("Courier", 26, 'bold'))

errorlabel = Label(master=root, foreground='#03328F', height=2, background='#FECE22') # Error label zodra onbekend locatie ingevoerd word.
errorlabel.configure(font=("Courier", 15, 'bold'))

Perron = Label(master=root, foreground='#03328F', height=2, background='#FECE22') # Perron: label
Perron.configure(font=("Courier", 12, 'bold'))


NLbuttonimg=ImageTk.PhotoImage(Image.open("images\\NL.png")) # Nederlands vlag hoofdmenu
buttonlanguageNL = Button(master=root, image=NLbuttonimg, height=60, width=89, background='Black',
                        foreground='white',
                        command=clickedNL)

UKbuttonimg=ImageTk.PhotoImage(Image.open("images\\EN.png")) # Engels vlag hoofdmenu
buttonlanguage = Button(master=root, image=UKbuttonimg, height=60, width=89, background='Black',
                        foreground='white',
                        command=clickedEN)

#eerste 3 buttons hoofdmenu
button1 = Button(master=root, height=3, width=19, background='#03328F',
                 foreground='white', command=error)
button1.configure(font=("Courier", 13, 'bold'))
button2 = Button(master=root, height=3, width=19, background='#03328F',
                 foreground='white', command=error)
button2.configure(font=("Courier", 13, 'bold'))
button3 = Button(master=root, height=3, width=19, background='#03328F',
                 foreground='white',
                 command=toonTweedeFrame)
button3.configure(font=("Courier", 13, 'bold'))

# Backspace voor toetsenbord
backspace = Button(root, text="backspace", height=2, width=18, background='#03328F', foreground='white',
             padx=2, pady=5, command=lambda: remove_letter())
backspace.configure(font=("Courier", 13, 'bold'))



# Button Ga terug naar hoofdmenu
backbutton2 = Button(master=root, height=3, width=19, background='#D2091A',
                     foreground='white', command=toonHoofdFrame, padx=20, pady=5)
backbutton2.configure(font=("Courier", 13, 'bold'))

# Button Huidige locatie
button4 = Button(master=root, height=3, width=19, background='#03328F',
                 foreground='white',
                 command=vertrek, padx=20, pady=5)
button4.configure(font=("Courier", 13, 'bold'))

# Button Andere locaties
button5 = Button(master=root, height=3, width=19, background='#03328F',
                 foreground='white',
                 command=overigeLocaties1, padx=20, pady=5)
button5.configure(font=("Courier", 13, 'bold'))


# Welkom bij NS NL hoofdmenu
img = ImageTk.PhotoImage(Image.open("images\\welkombijns.png"))
panel = Label(root, image=img, background='#FECE22')
panel.place(x=540, y=100)

# Welkom bij NS ENG hoofdmenu
pil_imageA = Image.open("images\\welkombijns_en.png")
imgA = ImageTk.PhotoImage(pil_imageA)
panelA = Label(root, image=imgA, background='#FECE22')

# Zoek balkje Andere locaties
entry = Entry(master=root)
entry.place(x=500, y=300)
large_font = ('Verdana',20)
entry.config(width=30, font=large_font)

# Zoek button
button6 = Button(master=root, height=1, width=19, background='#0079D3', command=zelfInvullen1, foreground='white')
button6.configure(font=("Courier", 13, 'bold'))

# Volgende 8 stations button binnen Andere locataies
button7 = Button(master=root, height=3, width=19, background='#03328F', foreground='white',
                 command=lambda: geef_labels(0))
button7.configure(font=("Courier", 13, 'bold'))

# Vorige 8 stations button binnen Andere locaties
button8 = Button(master=root, height=3, width=19, background='#03328F', foreground='white',
                 command=lambda: geef_labels(-2))
button8.configure(font=("Courier", 13, 'bold'))

# Zoek opnieuw button binnen Andere locaties
button9 = Button(master=root, height=1, width=19, background='#0079D3', command=overigeLocaties1, foreground='white')
button9.configure(font=("Courier", 13, 'bold'))

# Volgende 8 stations binnen Huidige locaties
button10 = Button(master=root, height=3, width=19, background='#03328F', foreground='white',
                 command=lambda: geef_labels1(0))
button10.configure(font=("Courier", 13, 'bold'))

# Vorige 8 locaties binnen Huidige locaties
button11 = Button(master=root, height=3, width=19, background='#03328F', foreground='white',
                 command=lambda: geef_labels1(-2))
button11.configure(font=("Courier", 13, 'bold'))

toonHoofdFrame() # Start met hoofd frame
root.mainloop()

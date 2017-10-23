def toonaantalkluizenvrij():
    with open('final assigment.py') as x:
        kluizen = 12 - sum(1 for aantal in x)
        return kluizen

def nieuwe_kluis():
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]

    infile = open('final assigment.py')
    lines = infile.readlines()
    infile.close()
    for regel in lines:
        gesplitste_regel = regel.split(';')
        nummer = gesplitste_regel[0]

        kluisnummers.remove(int(nummer))

    print('Beschikbare nummers: {}'.format(kluisnummers))

    if len(kluisnummers) > 0:
        nieuwe_nummer = kluisnummers[0]
        nieuwe_code = input('Geef een kluiscode op:')
        print('Uw kluisnummer is'+str(nieuwe_nummer))
        outfile = open('final assigment.py', 'a')
        outfile.write(str(nieuwe_nummer) + ';' + nieuwe_code + '\n')
        outfile.close()
    else:
        print('Geen kluizen beschikbaar')


def kluis_openen():
    kluisnummer = int(input('Vul uw kluisnummer in:'))
    wachtwoord = str(input('Vul uw wachtwoord in'))

    found = False
    infile = open('final assigment.py')
    lines = infile.readlines()
    for line in lines:
        if str(kluisnummer)+ ';'+str(wachtwoord) in line:
            found = True
            print('Correcte combinatie')
    infile.close()
    if found == False:
        print('Onjuiste combinatie')





print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')

optie = input('Welkom, voer uw keuze in:')

if optie == '1':
    print('Uw keuze is 1')
    print(toonaantalkluizenvrij())

elif optie == '2':
    print('Uw keuze is 2')
    print(nieuwe_kluis())


elif optie == '3':
    print('Uw keuze is 3')
    kluis_openen()

elif optie == '4':

    print('Uw keuze is 4')
else:
    print('Foute invoer programma stopt!')


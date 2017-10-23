def kaart():
    infile = open('kaartnummers.txt')
    kaartlees = infile.readlines()
    infile.close()

    kaartlijst = kaartlees

    for name in kaartlijst:
        fl = name.split(',')
        print('{} heeft kaartnummer: {}'.format(fl[1].strip(), fl[0]))

kaart()
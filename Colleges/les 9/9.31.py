import csv

with open('bestand.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')
    hoogste_gevonden_score_tot_nu_toe = 0

    naam = ''
    for row in reader:
        if int(row[2]) > hoogste_gevonden_score_tot_nu_toe:
            hoogste_gevonden_score_tot_nu_toe = int(row[2])
            naam = str(row[1])

    print('{} De hoogste score is {}'.format(naam, hoogste_gevonden_score_tot_nu_toe,))
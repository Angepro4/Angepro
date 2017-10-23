import datetime
import csv

bestand = 'inloggers.csv'
#gebruik hier een herhalingslus:
while True:
    naam = input("Wat is je achternaam? ")
    if naam == "einde":
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    print()

with open('inloggers.csv','a', newline = '') as myCSVFile:
    tijd = datetime.datetime.today()
    writer = csv.writer(myCSVFile, delimiter=";")
    writer.writerow((tijd, naam, voorl, gbdatum, email))

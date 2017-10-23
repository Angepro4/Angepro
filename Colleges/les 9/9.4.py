import csv

with open('Headers.csv','w') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter = ';',lineterminator = '\n')
    writer.writerow(('Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'))
    writer.writerow(('121','ABC123','Highlightpen','231','0.56'))
    writer.writerow(('123','PQR678', 'Nietmachine', '587', '9.99'))
    writer.writerow(('128','ZYX163','Bureaulamp','34','19.95'))
    writer.writerow(('137','MLK709','Monitorstandaard','66','32.50'))
    writer.writerow(('271','TRS665','Ipad hoes','155','19.01'))

with open('Headers.csv','r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter = ';',lineterminator = '\n')

    appel = 0
    duurste_product = 0
    naam = ''
    artikelnummer = 0
    voorraad = 9999999999
    totaalvoorraad = 0
    next(myCSVFile)
    for row in reader:
        appel = row[4]
        appel = float(appel)
        peer = row[3]
        peer = eval(peer)
        if appel > duurste_product:
            duurste_product = appel
            naam = str(row[2])
        if peer < voorraad:
            voorraad = peer
            artikelnummer = str(row[0])
        totaalvoorraad = totaalvoorraad + peer

    print('Het duurste artikel is Monitorstandaard en die kost ' + str(duurste_product) + ' Euro')
    print('Er zijn slechts ' + str(voorraad) + ' exemplaren in voorraad van het product met nummer ' + (artikelnummer))
    print('In totaal hebben wij ' + str(totaalvoorraad) + ' producten in ons magazijn liggen')














def inlezen_beginstation(stations):
    while True:
        begin = input('Wat is je beginstation?:')
        if begin in stations:
            break
        else:
            print('Foute invoer, probeer nogmaals!')

    return begin


def inlezen_eindstation(stations, beginstation):
    while True:
        eind = input('Wat is je eindstation?:')
        if eind in stations:
            break
        else:
            print('Foute invoer, probeer nogmaals!')

        if stations.index(eind) > stations.index(beginstation):
            break
        else:
            print('Foute invoer, probeer nogmaals!')


    return eind

def omroepen_reis(stations,beginstations,eindstation):
    index = stations.index(eindstation) - stations.index(beginstation)
    print('Het beginstation ' + beginstation + ' is het ' + str(stations.index(beginstation)) + ' in het traject.')
    print('Het eindstation ' + eindstation + ' is het ' + str(stations.index(eindstation))+ ' in het traject')
    print('De afstand bedraagt {} stations'.format(index))
    print('De prijs van je kaartje is ' + str((index * 5)) + ' euro')

    tussenstation = stations.index(beginstation)
    print("Jij stapt in de trein in: " + beginstation)
    while True:
        if tussenstation < stations.index(eindstation) -1:
            tussenstation = tussenstation + 1
            print("- " + stations[tussenstation])
        else:
            break
    print("Jij stapt uit in: " + eindstation)







stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '/s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

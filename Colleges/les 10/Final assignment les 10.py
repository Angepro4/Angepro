import xmltodict


def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary


stationsdict = processXML('stationslijst.xml')
stations = stationsdict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    print('{:5}- {}'.format(station['Code'], station['Type']))

print()
print('Dit zijn alle stations met één of meer synoniemen:')
for station in stations:
    if station['Synoniemen'] is not None:

        synoniemen = station['Synoniemen']
        print(synoniemen['Synoniem'][0])
        print(synoniemen['Synoniem'][1])

        print('{:5}- {}'.format(station['Code'], station['Synoniemen']))

print()
print('Dit is de lange naam van elk station:')
for station in stations:
    print('{:5}- {}'.format(station['Code'], station['Namen']['Lang']))

import requests
import xmltodict

def vertrekTijden():
    auth_details = ('yassine.benhadi@student.hu.nl', 'B9MtIu7EkzS9Jd14pOqTtwy3lBUlxlE0bbrCk-hHduGhOk3MSBCd9g')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=utrecht'
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    lst=[]
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]

        if 'VertrekVertragingTekst' in vertrek.keys():
            vertraging = vertrek['VertrekVertragingTekst'][0:2]
        else:
            vertraging = ''
        #routeTekst = vertrek['RouteTekst']
        #treinSoort = vertrek['TreinSoort']

        spoor = vertrek['VertrekSpoor']
        lst.append('{:<5}{:2} {:<23}  {:>3}'.format(vertrektijd, vertraging,  eindbestemming, spoor['#text']))
    return lst


#vertrekTijden()
#print(vertrekTijden())
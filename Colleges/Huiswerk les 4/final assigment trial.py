def standaardtarief(afstandKM):
    prijs = 0

    if afstandKM > 0 and afstandKM <= 50:
        prijs = 0.8 * afstandKM

    if afstandKM > 50:
        prijs = 15 + afstandKM * 0.6

    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    basisprijs = standaardtarief(int(afstandKM))




    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            basisprijs = basisprijs * 0.65
        else:
            basisprijs = basisprijs * 0.7

    else:
        if weekendrit == True:
            basisprijs = basisprijs * 0.6

    return basisprijs

leeftijd = int(input('Voer uw leeftijd in: '))
weekend = input('Is het een weekendrit?: ')

weekendRit = False
if weekend == 'ja':
    weekendRit = True

print(ritprijs(leeftijd, weekendRit,input('Wat is de afstand in Kilometers?: ')))










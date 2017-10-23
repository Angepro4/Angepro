def standaardtarief(afstandKM):
    afstandprijs = 0
    if afstandKM <= 0:
       afstandprijs = 0
    if afstandKM > 0 and afstandKM <= 50:
       afstandprijs = afstandKM * 0.8
    if afstandKM > 50:
       afstandprijs =(afstandKM * 0.6) + 15

    return afstandprijs

def ritprijs(leeftijd, weekendrit, afstandKM):

    if weekendrit == 'ja':
        if 12 <= int(leeftijd) < 65:
            weekendkorting = 0.6
        if int(leeftijd) < 12 or int(leeftijd) >= 65:
            weekendkorting = 0.65

    else:
        if 12 <= int(leeftijd) < 65:
             weekendkorting = 1
        if int(leeftijd) < 12 or int(leeftijd) >= 65:
             weekendkorting = 0.7

    afstandprijs = standaardtarief(int(afstandKM))

    eindprijs = afstandprijs * weekendkorting

    return eindprijs

prijs=ritprijs(input('Voer uw leeftijd in: '),input('Is het een weekendrit:? '),input('Wat is de afstand in Kilometers?: '))
print(prijs)

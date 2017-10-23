invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst1 = invoer.split('-')
lijst1.sort()

print('Gesorteerde lijst van ints:'+str(lijst1))
print('grootste getal: '+ max(lijst1)+' en het kleinste getal '+min(lijst1))
print('Aantal getallen: '+str(len(lijst1))+' en som van de getallen: '+str(sum(int(x) for x in lijst1)))
print('gemiddelde:'+str(sum(int(x) for x in lijst1) / len(lijst1)))


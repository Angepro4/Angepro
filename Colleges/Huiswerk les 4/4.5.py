import math
def kwadraten_som(grondgetallen):
   lijst = [0]
   for grondgetal in grondgetallen:
    if grondgetal >= 0:
       h = grondgetal**2
       lijst.append(h)

    x = sum(lijst)
    print (x)

print(kwadraten_som([4, 5, 3, -81]))



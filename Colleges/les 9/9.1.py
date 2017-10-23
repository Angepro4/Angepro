try:
    aantalpersonen = int(input('Met hoeveel personen bent u?'))
    perpersoon = 4356/aantalpersonen
    print(perpersoon)
except ZeroDivisionError:
    print('0 personen kan niet')
except ValueError:
    print('Er is geen geldige waarde ingevoerd')
except:
    print('Onjuiste invoer')






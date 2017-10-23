with open('hardlopers.txt', 'w') as myfile:
    myfile.write('Thu 10 Mar 2016, 10:45:52, Miranda')
    myfile.write('Thu 10 Mar 2016, 10:46:04, Piet')
    myfile.write('Thu 10 Mar 2016, 10:47:27, Sacha')
    myfile.write('Thu 10 Mar 2016, 10:48:33, Karel')
    myfile.write('Thu 10 Mar 2016, 10:48:42, Kemal')
    print(myfile.write)

weekday = 'thu'
month = 'march'
day ='10'
year = '2016'
hour = '10'
minute = '45'
second = '52'

waarde = ('{}:{}:{}'.format(hour, minute, second))
print(waarde)

print('{}, {} {}, {} at {}:{}:{}'.format(weekday, month, day, year, hour, minute, second))

import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a, %d, %b, %Y')
print(s)

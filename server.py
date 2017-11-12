import socket
import RPi.GPIO as GPIO
import time
import smtplib
from threading import *

# MAIL SETUP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("beveiliginghu@gmail.com", "Test12345")

alarmOn = 'Subject: {}\n\n{}'.format("Alarmsysteem ingeschakeld", "Er is beweging gedetecteerd, kijk op stream.davidabis.nl")

alarmOff = 'Subject: {}\n\n{}'.format("Alarmsysteem uitgeschakeld", "Hierbij krijgt u een bevestigings mail dat uw alarmsysteem is uitgeschakeld vanuit de server")

netwerkOff = 'Subject: {}\n\n{}'.format("Netwerkverbinding verbroken", "Er is geen verbinding meer tussen uw beveiligingssysteem en de alarmcentrale. Kijk op stream.devidabis.nl")

validatie = False

s = socket.socket()
host = ''
port = 12341

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def controler(): # Controleert op netwerkverbinding tussen server en client
        global validatie
        with open('/sys/class/net/eth0/operstate', 'r') as myfile:
            key2=myfile.read().replace('\n', '')
        if key2 =='up': # Indien verbinden intact is tussen server en client
            validatie = False
            GPIO.output(21, GPIO.LOW) # Blauw uit
        elif key2=='down': # indien er geen verbinden is tussen server en client 
            validatie = True
            kabelbreuk() #blauw aan
            print('Geen verbinding gedetecteerd!')
        Timer(10, controler).start() # timer om continue verbinding te testen


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Rood lampje 
GPIO.output(17, GPIO.LOW) # rood lampje uit
GPIO.setup(21, GPIO.OUT) # blauw lampje




def kabelbreuk(): 
        global validatie
        validatie = True
        if validatie == True: 
            GPIO.output(21, GPIO.HIGH) #Blauw lampje aan
            server.sendmail("Alarmsysteem", "abisnwo@gmail.com", netwerkOff) #verstuur waarschuwingsmail

controler()

s.listen(1)
while True: #Start MAIN whileloop
  c, addr = s.accept()
  print('Alarmsysteem is verbonden met: ',addr)
  c.send(b'U bent nu verbonden met het alarmsysteem.')
  message = c.recv(1024)
  if message == b'ROOD': #Ontvangt bericht vanuit client
     server.sendmail("Alarmsysteem", "abisnwo@gmail.com", alarmOn) # Verstuur mail indien alarm is ingeschakeld
     GPIO.output(17, GPIO.HIGH) # Rood lampje aan
     print('Alarm gaat af!') 
     while True: #GUI om alarm uit te schakelen
         print('Optie 1: Schakel alarm uit') # Schakelt alarm af
         print('Livestream client: stream.davidabis.nl')
         keuze = input('Maak een keuze: \n')
         if keuze == '1': # Uitschakelen alarm
             c.send(b'UIT') # Verstuur bericht naar client, die weer alarm uitzet.
             GPIO.output(17, GPIO.LOW) # Rood lampje uit
             print('Alarm is uitgeschakeld')
             server.sendmail("Alarmsysteem", "abisnwo@gmail.com", alarmOff) # verstuur mail bevestiging uitschakelen alarm vanuit server
             server.quit()
             break
         else: 
             continue
  c.send(b'ontvangen e')
  c.close()

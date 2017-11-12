import RPi.GPIO as GPIO
import time
import socket
from threading import *
import pygame
import os
import subprocess
import serial
pygame.init()


timeup= False
s = socket.socket()
host = '192.168.42.13'
port = 12341

def foo():
        print(time.ctime())

foo()

s.connect((host, port))
print(s.recv(1024))

def fase2(): # 20 Seconden voorbij, alarm aan.
        global timeup
        global code
        code = Timer(20.0, fase2)
        print('\n20 seconden voorbij, alarm ingeschakeld')
        s.send(b'ROOD')
        timeup = True
        pygame.mixer.music.load("alarm3.wav")  #Alarm geluid laden
        pygame.mixer.music.play()  #Alarm geluid afspelen
        message = s.recv(1024) # Bericht opvangen van de server
        if message == b'UIT': # Als de server alarm uitzet
            GPIO.output(18, GPIO.HIGH) # Groen lampje aan (clientside)
            GPIO.output(26, GPIO.LOW) # Geel lampje uit (clientside)
            pygame.mixer.music.stop()# Stop alarm geluid
            print('Alarmsysteem is vanuit de server uitgeschakeld.')
            s.send(b'UIT1')

code = Timer(20.0, fase2)
wachtwoord = '1234'
def fase1(): # Functie aan bij druk op knop (clientside)
        global timeup
        global code
        print('Waarschuwing: U heeft 20 seconden voordat het alarm wordt ingeschakeld.\n')
        print('Toon uw pas:')
        GPIO.output(26, GPIO.HIGH)# Geel aan
        GPIO.output(18, GPIO.LOW) # Groen uit
        count = 1
        code.start() # Timer 20 seconden voor code invoer
        while count < 4:
            if timeup == True:
                print('\n 20 seconden zijn voorbij. ')
                break
            pogingPasje = 0
            while pogingPasje <1:
                pasje = NFC()
                if pasje == True:
                    code.cancel()
                    code = Timer(10.0, fase2)
                    GPIO.output(26, GPIO.LOW) # Geel gaat uit
                    GPIO.output(18, GPIO.HIGH) # Groen gaat aan
                    print('\nPasje correct, alarm uitgeschakeld.\n')
                    break
                else:
                    pogingPasje +=1
                    pogingPincode = 1
                    print(' ')
                    print('\nPasje niet herkend, voer pincode in.\n')
                    while pogingPincode < 4:
                        print('\nPoging ' + str(pogingPincode) + ' van de 3\n')
                        invoer = input('\nVoer pincode in: \n ')
                        if invoer != wachtwoord:
                            pogingPincode += 1
                            continue
                        else: # Als code correct is
                            code.cancel() #stop timer
                            GPIO.output(26, GPIO.LOW)  #geel uit
                            GPIO.output(18, GPIO.HIGH) # groen aan
                            print('\nPincode correct, welkom.')
                            break
            break




ser = serial.Serial('/dev/ttyACM0') # Open serieel port
with open('key2', 'r') as myfile: # opent de key, bestand 'key2'
    key2 = myfile.readline(30) # inhoud wordt in een variabel gezet


def NFC():  #Uitlezen NFC pasje
        seq = []
        count = 1


        while True:
            for c in ser.read():
                seq.append(chr(c)) # converteren naar ASCII
                joined_seq = ''.join(str(v) for v in seq) # Maak string van een lijst
            if chr(c) == '\n':
                break

        if key2 in joined_seq: # Check waarde pasje
            return True  # Code komt overeen met inhoud key2
        else:
            return False  # Code komt niet overeen met inhoud waarde



validatie = False

def controler(): # Check of netwerkkabel nog verbinding maakt
        global validatie
        with open('/sys/class/net/eth0/operstate', 'r') as myfile:
            key2=myfile.read().replace('\n', '')
        if key2 =='up': # Indien netwerkverbinding tussen server en client intact is
            validatie = False
            GPIO.output(21, GPIO.LOW) # Blauw aan
        elif key2=='down': # Indien er geen verbinding is 
            validatie = True
            kabelbreuk() # Blauw lampje aan
            print('Geen verbinding gedetecteerd!')        
        Timer(10, controler).start()# Timer om verbinding continue te controlerenn om de 10 seconden

        

# Button starten
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) # GROEN lampje
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Knop
GPIO.setup(26, GPIO.OUT) # GEEL lampje
GPIO.output(26, GPIO.LOW) # Geel lampje
GPIO.output(18, GPIO.HIGH) #groen lampje
GPIO.setup(21, GPIO.OUT) # Blauw lampje



def kabelbreuk(): #netwerkkabel stuk/los
        global validatie
        validatie = True
        if validatie == True:
            GPIO.output(21, GPIO.HIGH) #blauw aan
 


controler()

while True: # Alles begint hier:
    input_state = GPIO.input(27) #knopje
    if not input_state: # Als knop wordt ingedrukt
        fase1() #start fase1
        time.sleep(3) 

s.close()

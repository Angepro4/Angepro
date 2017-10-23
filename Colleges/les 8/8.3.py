def code(invoerstring):
    ascistring = ""
    for letter in invoerstring:
        ascistring = ascistring + chr(ord(letter)+3)
    return ascistring

naam = str(input("Naam: "))
beginst = str(input("Beginstation: "))
eindst = str(input("Eindstation: "))
invoerstring = str(naam + beginst + eindst)

print(code(invoerstring))

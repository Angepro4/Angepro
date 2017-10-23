def letters():
    while True:
        woord = input('Geef een string van 4 letters:')
        x = len(woord)
        if len(woord) == 4:
            print('inlezen van correcte string: '+str((woord))+ ' is geslaagd')
            break
        else:
            print(str((woord)),' heeft '+str((x))+' letters')


letters()


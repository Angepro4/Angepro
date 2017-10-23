def som():
    condition = 0

    while True:
        getal = int(input('Geef een getal:'))
        if getal == 0:
            break

        condition = condition+getal
    return condition
print(som())

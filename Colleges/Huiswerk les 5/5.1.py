def convert(celsius):
    temperatuur = celsius * 1.8 + 32

    return temperatuur

def table(celsius):
    print('{:5} {:5}'.format('F','C'))

    for celsius in range(-30, 50)[::10]:
        temperatuur = convert(celsius)

        print('{:5} {:5}'.format(temperatuur, celsius))

        celsius + 10

    return celsius

celsiustable = table(-30)

print(celsiustable)


        #voor elke temperatuur convert aanroepen
        #print het resultaat '{} {}'.format(..., ...)


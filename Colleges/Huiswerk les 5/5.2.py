def kaart():
    example = open('kaartnummers.txt', 'w')
    example.write('325255, Jan Jansen 334343, Erik Materus 235434, Ali Ahson 645345, Eva Versteeg 534545, Jan de Wilde) 345355, Henk de Vries')
    kaartlijst = example.readline()
    example.close

    kaartlees = kaartlijst

    for name in kaartlees:
        example = name.split(',')
        print('{} heeft kaartnummer {}'.format(example[1].strip(), example[0]))

kaart()
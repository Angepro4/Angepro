infile = open('kaartnummers.txt')
def uitvoer(werknemers):
    for name in werknemers:
        x = name.split(',')
        print('{} heeft kaartnummer: {}'.format(x[1].strip(), x[0]))
    infile.close()
uitvoer(infile)
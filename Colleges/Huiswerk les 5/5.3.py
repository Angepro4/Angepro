def numlines('kaartnummers.txt.py'):
    'returns the number of lines in file filename'

    infile = open('kaartnummers.txt.py','r')
    linelist = infile.readlines()
    infile.close()

    return len(linelist)
    print(linelist)


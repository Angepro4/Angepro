with open('kaartnummers.txt') as file:
    data = file.readlines()

print('Deze file telt %s regels' % len(data))
print('Het grootste kaartnummer is: %s' % max(line.split(',')[0] for line in data))







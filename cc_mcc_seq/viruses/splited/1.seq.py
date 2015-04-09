import sys
D2 = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.fa', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2[fields[0]] = line
inFile.close()

if D2:
    D = dict()
    inFile = open('../split/'+sys.argv[1].split('.blasted.split')[0])
    for line in inFile:
        line = line.strip()
        if line.find('>') == 0:
            head = line.strip('>')
        else:
            D[head] = line
    inFile.close()

    for k in D2:
        ouFile.write('>'+k+'\n')
        ouFile.write(D[k]+'\n')



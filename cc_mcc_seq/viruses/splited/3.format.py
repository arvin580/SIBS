### ls *.blasted.m1 |xargs -n 1 python 3.format.py
import sys
D = dict()
inFile = open(sys.argv[1])
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], [])
    D[fields[0]].append('\t'.join(fields[1:3] + fields[6:10]))
inFile.close()

ouFile = open(sys.argv[1] + '.format', 'w')

if D:
    ouFile.write('#' + sys.argv[1].split('.')[0] + '\n')
    D2 = dict()
    inFile = open(sys.argv[1].split('.blasted.m1')[0])
    for line in inFile:
        line = line.strip()
        if line .find('>') != -1:
            head = line.strip('>')
        else:
            D2[head] = line
    inFile.close()

for k in D:
    ouFile.write('>' + k + '\n')
    ouFile.write(D2[k] + '\n')
    for item in D[k]:
        ouFile.write(item + '\n')
    ouFile.write('\n')

ouFile.close()

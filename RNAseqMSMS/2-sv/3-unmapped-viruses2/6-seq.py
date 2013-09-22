import sys
import os

files = os.listdir('.') 
D = {}
for f in files:
    if f[-9:] == '.unmapped':
        inFile = open(f)
        while True:
            line1 = inFile.readline().strip('>\n')
            line2 = inFile.readline().strip()
            if line1:
                D[line1] = line2
            else:
                break



        inFile.close()

def viruse(inF):
    D2  = {}
    inFile = open(inF)
    ouFile = open(inF + '.seq', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D2.setdefault(fields[0], [])
        D2[fields[0]].append(line)
    inFile.close()
    for k in D2:
        ouFile.write('>'+'\t'.join(D2[k])+'\n')
        ouFile.write(D[k]+'\n')
    ouFile.close()


viruse('unmapped-blated-viruses-90-60')




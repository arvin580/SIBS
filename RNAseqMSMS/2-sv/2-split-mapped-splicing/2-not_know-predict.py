import sys
import os
DIR='../2-split-mapped2'
files = os.listdir(DIR)
D = {}
for f in files:
    if f[-9:]=='.splicing':
        inFile = open(DIR+'/'+f)
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                D.setdefault(fields[0],[])
                D[fields[0]].append(line1)
                D[fields[0]].append(line2)
            else:
                break
        inFile.close()

D2={}
DIR='../2-split-mapped3'
files = os.listdir(DIR)
for f in files:
    if f[-9:]=='.splicing':
        inFile = open(DIR+'/'+f)
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                if fields[0] not in D:
                    D2.setdefault(fields[0],[])
                    D2[fields[0]].append(line1)
                    D2[fields[0]].append(line2)
            else:
                break
        inFile.close()
for k in D2:
    print('\t'.join(D2[k][0::2]))
    print('\t'.join(D2[k][1::2]))


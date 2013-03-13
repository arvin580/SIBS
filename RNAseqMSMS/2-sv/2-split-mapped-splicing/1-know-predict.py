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
                D.setdefault(fields[0],[])
                D[fields[0]].append(line1)
                D[fields[0]].append(line2)
            else:
                break
        inFile.close()
ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.known-predict','w')
for k in D:
    ouFile.write('\t'.join(D[k][0::2])+'\n')
    ouFile.write('\t'.join(D[k][1::2])+'\n')


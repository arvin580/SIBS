import sys
import os
DIR='../2-split-mapped2'
files = os.listdir(DIR)
D = {}
for f in files:
    if f[-13:]=='.not-splicing':
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
D2= {}
for f in files:
    if f[-13:]=='.not-splicing':
        inFile = open(DIR+'/'+f)
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                D2.setdefault(fields[0],[])
                D2[fields[0]].append(line1)
                D2[fields[0]].append(line2)
            else:
                break
        inFile.close()
ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.sv.known-predict','w')

for f in files:
    if f[-13:]=='.not-splicing':
        inFile = open(DIR+'/'+f)
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                if fields[0] in D and fields[0] in D2:
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')
            else:
                break
        inFile.close()
ouFile.close()

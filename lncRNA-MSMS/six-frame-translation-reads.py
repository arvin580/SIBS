#!/usr/bin/env python
import sys
import string

Codon = {}
inFile = open('CodonUsage')
for line in inFile:
    line = line.strip()
    fields = line.split()
    Codon[fields[0]]=fields[1]
inFile.close()

def translate(seq):
    six = []
    trans = string.maketrans('atcgATCG','tagcTAGC')
    seq1 = seq
    seq2 = string.translate(seq[::-1],trans)
    for i in range(3):
        pep = []
        for j in range(i,len(seq1),3):
            c = seq1[j:j+3]
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))
    '''
    for i in range(3):
        pep = []
        for j in range(i,len(seq2),3):
            c = seq2[j:j+3]
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))
    '''
        

    return six



inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.pep','w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        six = translate(line2)
        for i in range(len(six)):
            if six[i].find('*')==-1:
                ouFile.write(line1+'\t'+str(i)+'\n')
                ouFile.write(six[i]+'\n')
    else:
        break
inFile.close()
ouFile.close()

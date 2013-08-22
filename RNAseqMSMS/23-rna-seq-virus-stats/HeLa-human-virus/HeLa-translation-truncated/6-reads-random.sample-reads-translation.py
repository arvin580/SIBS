import string
import random

Codon = {}
inFile = open('/netshare1/home1/people/hansun/Data/CodonUsage')
for line in inFile:
    line = line.strip()
    fields = line.split()
    Codon[fields[0]]=fields[1]
inFile.close()

def translate(seq):
    six = []
    trans = string.maketrans('atcgATCG','tagcTAGC')
    seq1 = seq.upper()
    seq2 = string.translate(seq1[::-1],trans)
    for i in range(3):
        pep = []
        for j in range(i,len(seq1),3):
            c = seq1[j:j+3]
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))
    for i in range(3):
        pep = []
        for j in range(i,len(seq2),3):
            c = seq2[j:j+3]
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))
    return six 

D = {}
inFile = open('/netshare1/home1/people/hansun/Data/HeLa/Illumina/ERR0498-04-05.sam')
for line in range(95):
    inFile.readline()
for line in inFile:
    fields = line.split('\t')
    D[fields[0]] = fields[9]
inFile.close()

inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000-seq','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields:
        if D[item].find('N') == -1:
            ouFile.write(item+':'+':'.join(translate(D[item]))+'\t')
    ouFile.write('\n')
inFile.close()
ouFile.close()






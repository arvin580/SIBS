import sys
import os 
import string

def uniprot():
    uniprot = {}
    inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/3-uniprot/human_uniprot_sprot.fa')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            uniprot[line1]=line2
        else:
            break
    inFile.close()
    return uniprot

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
    seq1 = seq 
    seq2 = string.translate(seq[::-1],trans)
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

Dir = '../2-split-mapped'
files = os.listdir(Dir)
U = uniprot()
for f in files:
    if f[-4:]=='seq1':
        inFile = open(Dir+'/'+f)
        ouFile1 = open(f+'.splicing','w')
        ouFile2 = open(f+'.not-splicing','w')

        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                six = translate(line2)
                protein = ''
                for item in six:
                    for k in U:
                        if item in U[k]:
                            protein = [k.lstrip('>'),item]
                            break
                if protein:
                    ouFile1.write(line1+'\t'+protein[0]+'\t'+line2+'\n')
                    ouFile1.write(protein[1]+'\n')
                else:
                    for x in range(len(six)):
                        if six[x].find('*')==-1:
                            ouFile2.write(line1 + '\t'+ line2+ '\t'+ str(x)+ '\n')
                            ouFile2.write(six[x]+'\n')
            else:
                break
        inFile.close()
        ouFile1.close()
        ouFile2.close()

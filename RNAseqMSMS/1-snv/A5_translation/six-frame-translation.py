import sys
import string
from math import ceil

Codon = {}
inFile = open('/netshare1/home1/people/hansun/Data/CodonUsage')
for line in inFile:
    line = line.strip()
    fields = line.split()
    Codon[fields[0]]=fields[1]
inFile.close()

def translate(seq,start,end,FROM,TO):
    # start,end:count from 1.
    six = []
    trans = string.maketrans('atcgATCG','tagcTAGC')
    if seq[start-1:end]== FROM:
        seq_to = seq[0:start-1]+TO+seq[end:]
        seq_rev = string.translate(seq[::-1],trans)
        seq_to_rev = string.translate(seq_to[::-1],trans)
        print(seq)
        print(seq_rev)
        print(seq_to)
        print(seq_to_rev)

        for i in range(3):
            pep = []
            for j in range(i,len(seq),3):
                c = seq[j:j+3]
                if len(c) == 3:
                    pep.append(Codon[c])
            s = start - i
            e = end - i 
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])
        for i in range(3):
            pep = []
            for j in range(i,len(seq_rev),3):
                c = seq_rev[j:j+3]
                if len(c) == 3:
                    pep.append(Codon[c])
            s = len(seq_rev) - end + 1 - i
            e = len(seq_rev) - start + 1 - i
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])

        end = start + len(TO) - 1
        for i in range(3):
            pep = []
            for j in range(i,len(seq_to),3):
                c = seq_to[j:j+3]
                if len(c) == 3:
                    pep.append(Codon[c])
            s = start - i
            e = end - i 
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])
        for i in range(3):
            pep = []
            for j in range(i,len(seq_to_rev),3):
                c = seq_to_rev[j:j+3]
                if len(c) == 3:
                    pep.append(Codon[c])
            s = len(seq_to_rev) - end + 1 - i
            e = len(seq_to_rev) - start + 1 - i
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])

    
        return six

    else:
        print('warning:'+'\t'+seq)

#six = translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',)
#six = translate('CCGAGGCAGGGATCAAAGATCAGCCTA',11,15,'GATCA','AT')
#six = translate('CCGAGGCAGGGATCAAAGATCAGCCTA',11,11,'G','A')
#print(six)

def snv(inF):
    inFile = open('')
    inFile.close()





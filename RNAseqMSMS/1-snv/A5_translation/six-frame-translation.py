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
            print(s)
            print(e)
            six.append([''.join(pep),int(ceil(s/3)),int(ceil(e/3))])
        for i in range(3):
            pep = []
            for j in range(i,len(seq_rev),3):
                c = seq_rev[j:j+3]
                if len(c) == 3:
                    pep.append(Codon[c])
            six.append([''.join(pep),0,0])
    
        return six

    else:
        print('warning:'+'\t'+seq)

#six = translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',)
six = translate('CCGAGGCAGGGATCAAA',8,10,'AGG','A')
print(six)

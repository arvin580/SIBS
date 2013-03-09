import sys
import string

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
    seq1 = seq
    if seq[start-1:end]== FROM:
        seq1_to = seq[0:start-1]+TO+seq[end:]
        seq2 = string.translate(seq1[::-1],trans)
        seq2_to = string.translate(seq1_to[::-1],trans)
        print(seq1)
        print(seq2)
        print(seq1_to)
        print(seq2_to)
    else:
        print('warning:'+'\t'+seq)
    '''
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
    '''



#six = translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',)
six = translate('CCGAGGCAGGGATCAAA',8,10,'AGG','A')
print(six)

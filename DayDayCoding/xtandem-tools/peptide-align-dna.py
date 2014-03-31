###   python peptide-align-dna.py peptide-align-dna
import string
import sys

trans = string.maketrans('atcgATCG','tagcTAGC')

Codon = {}
inFile = open('/netshare1/home1/people/hansun/Data/CodonUsage')
for line in inFile:
    line = line.strip()
    fields = line.split()
    Codon[fields[0]]=fields[1]
inFile.close()

def translate(seq):
    six = []
    seq1 = seq.upper()
    seq2 = string.translate(seq1[::-1],trans)
    for i in range(3):
        pep = []
        for j in range(i,len(seq1),3):
            c = seq1[j:j+3]
            if len(c) == 3:
                pep.append(Codon.get(c,'*'))
        six.append(''.join(pep))
    for i in range(3):
        pep = []
        for j in range(i,len(seq2),3):
            c = seq2[j:j+3]
            if len(c) == 3:
                pep.append(Codon.get(c,'*'))
        six.append(''.join(pep))

    return six 


inFile = open(sys.argv[1])
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    if line1:
        pep = line2
        dna = line3
        dna_six = translate(dna)
        #print('\n'.join(dna_six))
        start = 0
        end = start
        while start < len(pep):
            while end < len(pep):
                flag = 0
                end += 1
                for f,p in enumerate(dna_six):
                    if pep[start:end] in p:
                        flag = 1
                        maxp = end
                        frame = f
                if flag == 0:      
                    p = pep[start:maxp]
                    start = maxp
                    end = start
                    if frame == 0:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 1:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3 + 1
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 2:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3 + 2
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 3:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    elif frame == 4:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3-1
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    elif frame == 5:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3-1
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    print(str(start_dna) + '\t' + str(end_dna))
                    print(p)
                    print(seq_dna)
                    break
            if end == len(pep):
                #print(pep[start:end])

                flag = 0
                for f,p in enumerate(dna_six):
                    if pep[start:end] in p:
                        flag = 1
                        maxp = end
                        frame = f
                if flag == 1:      
                    p = pep[start:maxp]
                    start = maxp
                    end = start
                    if frame == 0:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 1:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3 + 1
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 2:
                        start_pep = dna_six[frame].find(p)
                        end_pep = start_pep + len(p)
                        start_dna = start_pep*3 + 2
                        end_dna = start_dna + len(p)*3
                        seq_dna = dna[start_dna:end_dna]
                    elif frame == 3:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    elif frame == 4:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3-1
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    elif frame == 5:
                        start_pep = dna_six[frame].find(p)
                        end_dna = len(dna)-start_pep*3-1
                        start_dna = end_dna - len(pep)*3
                        seq_dna = dna[start_dna:end_dna]
                        seq_dna = seq_dna[::-1]
                        seq_dna = string.translate(seq_dna, trans)
                    print(str(start_dna) + '\t' + str(end_dna))
                    print(p)
                    print(seq_dna)
                break
    else:
        break

inFile.close()

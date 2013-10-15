import sys 
import string

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

inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa','w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    
    info = fields[0] + ':' + fields[1]
    for i in range(10,len(fields),26):
        pos1 = fields[i]
        pos2 = fields[i+1]
        pos3 = fields[i+12]
        pos4 = fields[i+13]
        point = sorted([int(pos1),int(pos2),int(pos3),int(pos4)])[1]
        seq = fields[i+18].split('|')[0]
        seq_id = fields[i-6]
        six = translate(seq)
        for i in range(len(six)):
            if six[i].find('*')==-1:
                if i in [0,1,2]:
                    point_peptide = (point - 1 - i)/3 + 1
                    ouFile.write('>'+info+'\t'+seq_id+'\t'+str(point)+'\t'+'\t'.join([pos1,pos2,pos3,pos4])+'\t'+str(i)+'\t'+seq+'\t'+str(point_peptide)+'\n')
                    ouFile.write(six[i]+'\n')
                elif i in [3,4,5]:
                    point_peptide = (len(seq) - point  - i + 3 )/3 + 1
                    ouFile.write('>'+info+'\t'+seq_id+'\t'+str(point)+'\t'+'\t'.join([pos1,pos2,pos3,pos4])+'\t'+str(i)+'\t'+seq +'\t'+str(point_peptide)+'\n')
                    ouFile.write(six[i]+'\n')

inFile.close()

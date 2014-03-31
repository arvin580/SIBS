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
            c = seq1[j:j+3].upper()
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))
    for i in range(3):
        pep = []
        for j in range(i,len(seq2),3):
            c = seq2[j:j+3].upper()
            if len(c) == 3:
                pep.append(Codon[c])
        six.append(''.join(pep))

    return six 



import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
D = {}
inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1[1:]] = line2
    else:
        break
inFile.close()

inFile = open('HeLa-Peptide-Validation-non_blast2')
ouFile = open('HeLa-Peptide-Validation-non_blast2.fa', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split(':')
        ch = fields[0][1:]
        start = int(fields[1])
        end = int(fields[2])
        seq = D[ch][start-1:end]
        ouFile.write(line1 + '\n')
        ouFile.write(line2 + '\n')
        ouFile.write(seq + '\n')
        six = translate(seq)
        ouFile.write('\n'.join(six) + '\n')
    else:
        break

        
inFile.close()
ouFile.close()

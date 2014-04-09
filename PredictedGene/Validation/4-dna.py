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
inFile = open('ERR0498-04-05-DNA2')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split(':')
        dna = fields[1]
        dna_rev = dna[::-1]
        dna_rev = string.translate(dna_rev, trans)
        D.setdefault(dna, [])
        D[dna].append(line2)
        D.setdefault(dna_rev, [])
        D[dna_rev].append(line2)
    else:
        break
inFile.close()

Protein = {}
inFile2 = open('/netshare1/home1/people/hansun/PredictedGene/Homo_sapiens.GRCh37.75.pep.abinitio.fa.fa')
while True:
    line1 = inFile2.readline().strip()
    line2 = inFile2.readline().strip()
    if line1:
        Protein[line1] = line2
    else:
        break


inFile2.close()

inFile = open('HeLa-Peptide-Validation-2.txt')
for line in inFile:
    line = line.strip()
    fields = line.split()
    dna = fields[1]
    if dna in D:
        seq = D[dna]
        for s in seq:
            if s.find('N') == -1:
                six = translate(s)
                for x in six:
                    for k in Protein:
                        if x in Protein[k]:
                            print(dna + '\t' + s + '\t' + x + '\t' + k)

inFile.close()

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

inFile = open('x')
ouFile = open('x-pep', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        six = translate(line2)
        ouFile.write(line1 + '\n')
        ouFile.write(line2 + '\n')
        ouFile.write('\n'.join(six) + '\n')
    else:
        break
inFile.close()
ouFile.close()


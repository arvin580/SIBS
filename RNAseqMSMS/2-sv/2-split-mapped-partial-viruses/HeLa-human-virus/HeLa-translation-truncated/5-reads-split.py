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


Ensembl = {}
inFile = open('/netshare1/home1/people/hansun/Data/Ensembl/Homo_sapiens.GRCh37.70.pep.all.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        Ensembl[line1]=line2
    else:
        break
inFile.close()
print(len(Ensembl))

inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-split','w')


while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        ch1 = fields[3]
        ch2 = fields[15]
        pos1_query = int(fields[8])
        pos2_query = int(fields[9])
        pos3_query = int(fields[20])
        pos4_query = int(fields[21])
        pos1_subject = int(fields[10])
        pos2_subject = int(fields[11])
        pos3_subject = int(fields[22])
        pos4_subject = int(fields[23])
        seq1 = line2[pos1_query-1:pos2_query]
        seq2 = line2[pos3_query-1:pos4_query]
        seq1_six = translate(seq1)
        seq2_six = translate(seq2)
        flag1 = []
        flag2 = []
        for i in range(len(seq1_six)):
            for k in Ensembl:
                if seq1_six[i] in Ensembl[k]:
                    flag1.append(str(i))
        for i in range(len(seq2_six)):
            for k in Ensembl:
                if seq2_six[i] in Ensembl[k]:
                    flag2.append(str(i))
        flag1 = ''.join(flag1)
        flag2 = ''.join(flag2)

        ouFile.write(line1+'\t'+line2+'\t'+str(pos1_query)+':'+str(pos2_query)+':'+seq1+':'+':'.join(seq1_six)+':'+flag1+'\t'+str(pos3_query)+':'+str(pos4_query)+':'+seq2+':'+':'.join(seq2_six)+':'+flag2+'\n')



    else:
        break
inFile.close()

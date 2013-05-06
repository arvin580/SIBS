MSMS = {}
inFile = open('HeLa-Predict-pep.transcript')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    MSMS[fields[0]]=int(fields[1])
inFile.close()

RNASEQ = {}
inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/2-sv/2-split-mapped-splicing/ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict.transcript')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    RNASEQ[fields[0]]=int(fields[1])
inFile.close()

RNASEQ_MSMS = set(RNASEQ) & set(MSMS)

D = {}

inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split()
        for item in fields:
            if item.find('GENSCAN')==0:
                D.setdefault(item,[])
                D[item].append(line1+'\t'+line2)
    else:
        break
inFile.close()

inFile = open('HeLa-Predict-pep')
for line in inFile:
    line = line.strip()
    fields = line.split()
    for item in fields:
        if item.find('GENSCAN')==0:
            D.setdefault(item,[])
            D[item].append(line)
inFile.close()

ouFile = open('HeLa-predict-rnaseq-msms','w')

for k in RNASEQ_MSMS:
    ouFile.write(k+'\t'+'\t'.join(D[k])+'\n')



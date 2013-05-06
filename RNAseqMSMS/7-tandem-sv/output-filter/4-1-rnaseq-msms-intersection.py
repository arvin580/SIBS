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
print(len(RNASEQ_MSMS))



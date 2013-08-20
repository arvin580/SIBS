inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fa.blated-90-60')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D['>'+fields[0]] = 1
inFile.close()

inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing')
ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing-from-protein-mrna','w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        if fields[0] not in D:
            ouFile.write(line1+'\n')
            ouFile.write(line2+'\n')
    else:
        break
inFile.close()
ouFile.close()

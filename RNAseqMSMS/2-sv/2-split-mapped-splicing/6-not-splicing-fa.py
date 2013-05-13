D = {}
inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        D[fields[2]] = fields[26]
    else:
        break
inFile.close()

ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fasta','w')
for k in D:
    ouFile.write('>'+k+'\n')
    ouFile.write(D[k]+'\n')
ouFile.close()

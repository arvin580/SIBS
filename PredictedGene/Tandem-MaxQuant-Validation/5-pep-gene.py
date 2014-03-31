D = {}
inFile = open('/netshare1/home1/people/hansun/PredictedGene/Homo_sapiens.GRCh37.75.pep.abinitio.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split()
        geneid = fields[0][1:]
        genepos = 'chr'+':'.join(fields[2].split(':')[2:])
        D.setdefault(line2, [])
        D[line2].append(geneid+':'+genepos) 
    else:
        break
inFile.close()


inFile = open('HeLa-Peptide-Validation.txt')
ouFile = open('HeLa-Peptide-Validation-gene', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    pep = fields[0]
    ouFile.write(pep + '\t')
    for k in D:
        if pep in k:
            ouFile.write('\t'.join(D[k])+'\t')
    ouFile.write('\n')
inFile.close()
ouFile.close()

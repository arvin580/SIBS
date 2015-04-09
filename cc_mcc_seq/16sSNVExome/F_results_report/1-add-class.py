D = {}
inFile = open('sum_snv16sExome.genome_summary')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[21]+'\t'+fields[22]
    D[k]=fields[2]
inFile.close()

inFile = open('SNV.genome.somatic.nonsynonymous.UTR.ncRNA.geneLevel.recurrent.mutation')
ouFile = open('SNV.genome.somatic.nonsynonymous.UTR.ncRNA.geneLevel.recurrent.mutation.final','w')
for line in inFile:
    fields = line.split('\t')
    k = fields[1]+'\t'+fields[2]
    ouFile.write(D[k]+'\t'+line)
inFile.close()
ouFile.close()

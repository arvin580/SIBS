inFile = open('SNV.genome.somatic.ncRNA.geneLevel.ranksum_test.mutation.mc')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()

inFile = open('SNV.genome.somatic.ncRNA.geneLevel.ranksum_test')
ouFile = open('SNV.genome.somatic.ncRNA.geneLevel.ranksum_test.mc','w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    if fields[1] in D:
        ouFile.write(line+'\n')
inFile.close()
ouFile.close()

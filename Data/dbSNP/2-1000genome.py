inFile = open('hg19_snp137.txt')
ouFile = open('hg19_snp137_1000genome.txt','w')
for line in inFile:
    if line.find('1000GENOMES')!=-1: 
        fields = line.split('\t')
        ouFile.write('\t'.join(fields[1:5])+'\n')
inFile.close()
ouFile.close()

def gene(inF):
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    D = {}
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[1]]=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
gene('SNV.genome.somatic.nonsynonymous.UTR.ncRNA.geneLevel.recurrent.mutation.final')
gene('SNV.genome.somatic.nonsynonymous.UTR.ncRNA.geneLevel.recurrent.mutation.both')

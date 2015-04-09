def get_gene(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.gene','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        ouFile.write(fields[0]+'\n')
    inFile.close()
    ouFile.close()
get_gene('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel')
get_gene('SNV.exome.somatic.nonsynonymous.geneLevel')


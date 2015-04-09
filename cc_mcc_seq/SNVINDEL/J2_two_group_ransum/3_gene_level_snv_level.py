def gene2mutation(iFile1,iFile2):
    inFile=open(iFile1)
    ouFile=open(iFile1+'.mutation','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        gene=fields[1]
        inFile1=open(iFile2)
        for li in inFile1 :
            li=li.strip()
            fds=li.split('\t')
            if fds[0]==gene :
                ouFile.write(li+'\n')
        inFile1.close()
    inFile.close()
    ouFile.close()

gene2mutation('genome.somatic.exome.UTR.INDEL.nondbsnp.geneLevel.ranksum_test','genome.somatic.exome.UTR.INDEL.nondbsnp')

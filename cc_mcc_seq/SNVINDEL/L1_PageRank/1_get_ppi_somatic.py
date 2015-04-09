def get_gene(oFile):
    dict1=dict()
    inFile=open('SNV.genome.somatic.exome.UTR.geneLevel')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1[fields[0]]=1
    inFile.close()
    inFile=open('BINARY_PROTEIN_PROTEIN_INTERACTIONS.txt')
    ouFile=open(oFile,'w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if fields[0] in dict1  or fields[3] in dict1 :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()


get_gene('PPI_somatic')




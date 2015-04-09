def uniqueList(inList):
    ouList=list()
    for item in inList :
        if item not in ouList :
            ouList.append(item)
    return ouList



def snv_level_to_gene_level(iFile,sampleNum) :
    pass
    inFile=open(iFile)
    ouFile=open(iFile+'.geneLevel','w')
    dict1=dict()
    list1=list()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1.setdefault(fields[0],[0]*sampleNum)
        list1.append(fields[0])
        for i,item in enumerate(fields[-sampleNum:]) :
            dict1[fields[0]][i]+=int(item)
    for item in uniqueList(list1) :
        ouFile.write(item+'\t'+'\t'.join([str(x) for x in dict1[item]])+'\n')

    inFile.close()
    ouFile.close()

snv_level_to_gene_level('SNV.genome.somatic.UTR',8)


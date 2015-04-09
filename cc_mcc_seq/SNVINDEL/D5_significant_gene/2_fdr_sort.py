def fdr_sort(iFile) :
    dict1=dict()
    inFile=open(iFile)
    ouFile=open(iFile+'.sorted','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1[line]=float(fields[0])
    inFile.close()

    d=dict1.items()
    d.sort(cmp=lambda x,y :cmp(x[1],y[1]))

    for item in d :
        ouFile.write(item[0]+'\n')
    ouFile.close()

fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.CHC.fisher_test.fdr')
fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.ICC.fisher_test.fdr')
fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.ICC_CHC.fisher_test.fdr')


fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.CHC.fisher_test')
fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.ICC.fisher_test')
fdr_sort('SNV.exome.somatic.nonsynonymous_nondbsnp.geneLevel.ICC_CHC.fisher_test')

def somatic_pagerank(dict1,dict2,dict3) :
    inFile=open('hg19_max_coding_length')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict3[fields[0]]=int(fields[1])
    inFile.close()

    inFile=open('PPI_somatic.pageranked')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1[fields[0]]=float(fields[1])
    inFile.close()

    inFile=open('sum_snp.exome_summary.pass012.nonsynonymous.somatic.gene_level')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        gene=fields[0]
        val=sum([int(x) for x in fields[-8:]])/float(dict3[gene])
        dict2[gene]=val*dict1.get(gene,0)
    inFile.close()

dict1=dict()
dict2=dict()
dict3=dict()
somatic_pagerank(dict1,dict2,dict3)

d=dict2.items()
d.sort(cmp=lambda x,y :cmp(x[1],y[1]),reverse=True)
for item in d : 
    print(item[0]+'\t'+str(item[1]))




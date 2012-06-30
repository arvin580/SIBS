from RefGene_class import *

inFile=open('hg19_refGene.txt')
dict1=dict()
for line in inFile :
    refGene=RefGene()
    refGene.read_one_gene(line)
    refGene.gene_to_coding()
    N=refGene.gene_name()
    L=refGene.coding_length()
    dict1.setdefault(N,[])
    dict1[N].append(L)
inFile.close()

ouFile1=open('hg19_coding_length','w')
ouFile2=open('hg19_max_coding_length','w')

d=dict1.items()
d.sort(cmp=lambda x,y:cmp(max(x[1]),max(y[1])),reverse=True)
for item in d :
    ouFile1.write(item[0]+'\t'+'\t'.join([str(x) for x in item[1]])+'\n')
    ouFile2.write(item[0]+'\t'+str(max(item[1]))+'\n')




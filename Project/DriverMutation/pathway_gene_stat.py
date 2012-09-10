#!/usr/bin/env python

inFile1=open('pathway_gene','r')
ouFile1=open('pathway_gene_stat','w')
ouFile2=open('pathway_gene_stat2','w')

total=0
gene=dict()
for line in inFile1 :
    pg=line.split()
    gn=len(pg)-1
    ouFile1.write(str(gn)+'\n')
    total+=gn
    for item  in pg[1:] :
        gene.setdefault(item,0)
        gene[item]+=1

inFile1.close()
ouFile1.write('###\n')
ouFile1.write(str(total)+'\n')
ouFile1.write('###\n')

total=0
for key in gene :
    ouFile2.write(key+'\t'+str(gene[key])+'\n')
    total+=gene[key]
ouFile1.write(str(total)+'\n')

#!/usr/bin/env python

from SOAPpy import WSDL

wsdl = 'http://soap.genome.jp/KEGG.wsdl'
serv = WSDL.Proxy(wsdl)

results = serv.get_genes_by_pathway('path:eco00020')

###################################
pw_n=list()
pw_gene=dict()
pw=serv.list_pathways('hsa')

for i in range(len(pw)) :
    p=pw[i]['entry_id']
    pw_n.append(p)
    pw_gene[p]=serv.get_genes_by_pathway(p)

inFile1=open('pathway_gene','w')
for key in pw_gene :
    inFile1.write(key+'\t')
    inFile1.write('\t'.join(pw_gene[key])+'\n')


    






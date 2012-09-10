from SOAPpy import WSDL

ouFile1=open('kegg_pathway','w')
ouFile2=open('kegg_gene_raw','w')
ouFile3=open('kegg_gene','w')

wsdl = 'http://soap.genome.jp/KEGG.wsdl'
serv = WSDL.Proxy(wsdl)

results = serv.list_pathways('hsa')
for item in results :
    ouFile1.write(item[0]+'\t'+item[1]+'\n')
    genes=serv.get_genes_by_pathway(item[0])
    ouFile2.write(item[0]+'\t'+'\t'.join(genes)+'\n')
    ouFile3.write(item[0].split(':')[1]+'\t'+'\t'.join([gene.split(':')[1] for gene in genes])+'\n')

ouFile1.close()
ouFile2.close()
ouFile3.close()

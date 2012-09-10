inFile1=open('/netshare1/home1/people/hansun/Data/GeneID/gene_info_9606','r')
ouFile1=open('/netshare1/home1/people/hansun/Data/GeneID/gene_info_9606_symbol','w')

gene=list()
n=0
for line in inFile1 :
    fields=line.split()
    gene.append([])
    alias=fields[4].split('|')
    gene[n]=gene[n]+[fields[1]]+[fields[2]]+alias
    n+=1
inFile1.close()

for item in gene :
    ouFile1.write('\t'.join(item)+'\n')

inFile1=open('/netshare1/home1/people/hansun/Data/GeneID/gene_info_9606','r')

gene=list()
n=0
for line in inFile1 :
    fields=line.split()
    gene.append([])
    alias=fields[4].split('|')
    gene[n]=gene[n]+[fields[1]]+[fields[2]]+alias
    n+=1
inFile1.close()

#for item in gene :
#    ouFile1.write('\t'.join(item)+'\n')


def idmapping(file):
    inFile1=open(file,'r')
    
    ouFile1=open(file+'_found','w')
    ouFile2=open(file+'_notfound','w')
    
    for line in inFile1 :
        line=line.strip()
        fields=line.split('\t')
        for item in fields :
            flag=0
            for i in gene :
                for j in i :
                    #s=re.search('^'+item+'$',j,re.I) 
                    if j.lower()==item.lower():
                        ouFile1.write(item+'\t'+'\t'.join(i)+'\n')
                        flag+=1
                        break
            if flag==0 :
                ouFile2.write(item+'\n')
    
    inFile1.close()

idmapping('gene_symbol_stemcell')
idmapping('gene_symbol_inflammation')
idmapping('gene_symbol_metastasis')

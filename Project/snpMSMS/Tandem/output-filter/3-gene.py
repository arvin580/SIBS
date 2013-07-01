L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

def gene_dbsnp(inF):
    inFile = open(inF)
    ouFile = open(inF+'-gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch= fields[1].split(':')[1]
        pos1= fields[1].split(':')[2]
        pos2= fields[1].split(':')[3]
        
        genes = []

        for item in L:
            if (item[2]==ch and (int(item[4])<=int(pos1)<=int(item[5]) or int(item[4])<=int(pos2)<=int(item[5]))) :
                gene = item[12]
                genes.append(gene)
        ouFile.write(fields[0]+'\t'+'|'.join(set(genes))+'\t'+'\t'.join(fields[1:])+'\n')

    inFile.close()
    ouFile.close()

gene_dbsnp('Liver-SNV-INDEL-new-pep')

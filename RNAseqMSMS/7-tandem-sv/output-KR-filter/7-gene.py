L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

def gene_dbsnp(inF):
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            if item.find('genscan')!=-1:
                '''
                nc= item.split(':')[4]
                ch = item.split(':')[16]
                pos1_nc = item.split(':')[11]
                pos2_nc = item.split(':')[12]
                pos3_ch = item.split(':')[23]
                pos4_ch = item.split(':')[24]
        
                pos5_nc_query = item.split(':')[9]
                pos6_nc_query = item.split(':')[10]
                pos7_ch_query = item.split(':')[21]
                pos8_ch_query = item.split(':')[22]
                '''
                ch ='chr'+item.split(':')[3]
                pos1 =item.split(':')[4]
                pos2 =item.split(':')[5]
                genes = []
                for item in L:
                    if (item[2]==ch and (int(item[4])<=int(pos1)<=int(item[5]) or int(item[4])<=int(pos2)<=int(item[5]))) :
                        gene = item[12]
                        genes.append(gene)
                ouFile.write(fields[0]+'\t'+'|'.join(set(genes))+'\t'+'\t'.join(fields[1:])+'\n')
                break

    inFile.close()
    ouFile.close()

#gene_dbsnp('HeLa-SV-Duplication-pep')
#gene_dbsnp('HeLa-SV-Inversion-pep')
#gene_dbsnp('HeLa-SV-Deletion-pep')
#gene_dbsnp('HeLa-SV-Translocation-pep')
#gene_dbsnp('HeLa-Predict-Splicing-pep')
gene_dbsnp('HeLa-Predict-pep')

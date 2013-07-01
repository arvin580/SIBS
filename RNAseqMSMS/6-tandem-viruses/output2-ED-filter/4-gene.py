L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

GENE={}
GENE['E1']=[914,2887]
GENE['E2']=[2817,3914]
GENE['E4']=[3418,3684]
GENE['E5']=[3936,4157]
GENE['E6']=[105,581]
GENE['E7']=[590,907]
GENE['L1']=[5430,7136]
GENE['L2']=[4244,5632]
GENE['LCR']=[0,104]


def gene_dbsnp(inF):
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        nc= fields[1].split(':')[4]
        ch = fields[1].split(':')[16]
        pos1_nc = fields[1].split(':')[11]
        pos2_nc = fields[1].split(':')[12]
        pos3_ch = fields[1].split(':')[23]
        pos4_ch = fields[1].split(':')[24]

        pos5_nc_query = fields[1].split(':')[9]
        pos6_nc_query = fields[1].split(':')[10]
        pos7_ch_query = fields[1].split(':')[21]
        pos8_ch_query = fields[1].split(':')[22]
        genes1 = []
        genes2 = []

        for item in L:
            if (item[2]==ch and (int(item[4])<=int(pos3_ch)<=int(item[5]) or int(item[4])<=int(pos4_ch)<=int(item[5]))) or \
                   (item[2]==nc and (int(item[4])<=int(pos1_nc)<=int(item[5]) or int(item[4])<=int(pos2_nc)<=int(item[5])))  :
                gene = item[12]
                genes1.append(gene)
        for k in GENE:
            if (ch == 'NC_001357.1' and(int(GENE[k][0])<=int(pos3_ch)<=int(GENE[k][1]) or int(GENE[k][0])<=int(pos4_ch)<=int(GENE[k][1]))) or \
                    (nc == 'NC_001357.1' and(int(GENE[k][0])<=int(pos1_nc)<=int(GENE[k][1]) or int(GENE[k][0])<=int(pos2_nc)<=int(GENE[k][1]))) :
                gene = k
                genes2.append(gene)
        if genes1 and genes2:
            genes = '|'.join(set(genes1))+':'+'|'.join(set(genes2))
        elif genes1:
            genes = '|'.join(set(genes1))+':'+'*'
        else:
            genes = '*'+':'+'|'.join(set(genes2))

            
        ouFile.write(fields[0]+'\t'+genes+'\t'+ch+'\t'+nc+'\t'+pos3_ch+'\t'+pos4_ch+'\t'+pos1_nc+'\t'+pos2_nc+'\t'+pos7_ch_query+'\t'+pos8_ch_query+'\t'+pos5_nc_query+'\t'+pos6_nc_query+'\t'+fields[1]+'\n')


    inFile.close()
    ouFile.close()

gene_dbsnp('HeLa-Human-Viruses-pep')

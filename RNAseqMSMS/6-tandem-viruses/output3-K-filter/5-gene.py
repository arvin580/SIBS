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
        nc= fields[1].split(':')[2]
        #ch = fields[1].split(':')[16]
        pos1_nc = fields[1].split(':')[9]
        pos2_nc = fields[1].split(':')[10]
        #pos3_ch = fields[1].split(':')[23]
        #pos4_ch = fields[1].split(':')[24]

        pos5_nc_query = fields[1].split(':')[7]
        pos6_nc_query = fields[1].split(':')[8]
        #pos7_ch_query = fields[1].split(':')[21]
        #pos8_ch_query = fields[1].split(':')[22]
        genes = []
        for k in GENE:
            if GENE[k][0]<=int(pos1_nc)<=GENE[k][1] or GENE[k][0]<=int(pos2_nc)<=GENE[k][1]:
                genes.append(k)

        #ouFile.write(fields[0]+'\t'+'|'.join(set(genes))+'\t'+ch+'\t'+nc+'\t'+pos3_ch+'\t'+pos4_ch+'\t'+pos1_nc+'\t'+pos2_nc+'\t'+pos7_ch_query+'\t'+pos8_ch_query+'\t'+pos5_nc_query+'\t'+pos6_nc_query+'\t'+fields[1]+'\n')
        ouFile.write(fields[0]+'\t'+'|'.join(set(genes))+'\t'+nc+'\t'+pos1_nc+'\t'+pos2_nc+'\t'+pos5_nc_query+'\t'+pos6_nc_query+'\t'+fields[1]+'\n')


    inFile.close()
    ouFile.close()

gene_dbsnp('HeLa-Viruses-pep')

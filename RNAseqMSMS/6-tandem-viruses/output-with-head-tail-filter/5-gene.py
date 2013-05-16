def gene_dbsnp(inF):
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        nc= fields[1].split(':')[2]
        #ch = fields[1].split(':')[16]
        pos1_nc = fields[1].split(':')[7]
        pos2_nc = fields[1].split(':')[8]
        #pos3_ch = fields[1].split(':')[23]
        #pos4_ch = fields[1].split(':')[24]

        pos5_nc_query = fields[1].split(':')[9]
        pos6_nc_query = fields[1].split(':')[10]
        #pos7_ch_query = fields[1].split(':')[21]
        #pos8_ch_query = fields[1].split(':')[22]
        genes = []
        '''
        for item in L:
            if item[2]==ch and (int(item[4])<=int(pos3_ch)<=int(item[5]) or int(item[4])<=int(pos4_ch)<=int(item[5])):
                gene = item[12]
                genes.append(gene)
        '''
        #ouFile.write(fields[0]+'\t'+'|'.join(set(genes))+'\t'+ch+'\t'+nc+'\t'+pos3_ch+'\t'+pos4_ch+'\t'+pos1_nc+'\t'+pos2_nc+'\t'+pos7_ch_query+'\t'+pos8_ch_query+'\t'+pos5_nc_query+'\t'+pos6_nc_query+'\t'+fields[1]+'\n')
        ouFile.write(fields[0]+'\t'+nc+'\t'+pos1_nc+'\t'+pos2_nc+'\t'+pos5_nc_query+'\t'+pos6_nc_query+'\t'+fields[1]+'\n')


    inFile.close()
    ouFile.close()

gene_dbsnp('HeLa-Viruses-pep')

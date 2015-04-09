inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.0.05.2')

ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat','w')

dict1=dict()
for line in inFile :
    line=line.strip()
    gene=line.split('\t')[0]

    inFile1=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus')

    for line in inFile1 :
        line=line.rstrip()
        fields=line.split('\t')
        if fields[10] == gene :
            ouFile.write(line+'\n')


    inFile1.close()


inFile.close()

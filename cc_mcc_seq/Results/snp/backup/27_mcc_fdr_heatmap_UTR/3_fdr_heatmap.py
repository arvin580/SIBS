inFile=open('gene_fdr_0.01_c')

ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.gene_ttest_heat','w')

dict1=dict()
for line in inFile :
    line=line.strip()
    gene=line.split('\t')[0]

    inFile1=open('sum_snp.genome_combined.sorted.pass012.new.UTR.gene_ttest')

    for line in inFile1 :
        line=line.strip()
        fields=line.split('\t')
        if fields[0] == gene :
            ouFile.write('\t'.join(fields[0:1]+fields[12:])+'\n')


    inFile1.close()


inFile.close()

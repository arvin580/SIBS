def somatic_cmp_dbsnp(iFile1,iFile2) :
    dict1=dict()
    dict2=dict()
    inFile=open(iFile2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        dict1[k]=fields[8]
    inFile.close()

    inFile=open(iFile1)
    ouFile=open(iFile1+'.new','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        if k in dict1:
            if dict1[k].find('rs')==-1 :
                ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

#
somatic_cmp_dbsnp('SNV.genome.somatic.ICC4','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.ICC5','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.ICC9','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.ICC10','sum_snp.genome_summary.012')
##
##
somatic_cmp_dbsnp('SNV.genome.somatic.CHC5','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.CHC6','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.CHC7','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.somatic.CHC10','sum_snp2.genome_summary.012')

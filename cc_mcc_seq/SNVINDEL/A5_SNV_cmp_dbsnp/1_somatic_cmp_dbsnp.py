def somatic_cmp_dbsnp(iFile1,iFile2) :
    dict1=dict()
    dict2=dict()
    inFile=open(iFile2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        dict1[k]=fields[8]
        dict2[k]=fields[28]
    inFile.close()

    dbsnp132=0
    dbsnp135=0
    row=0

    inFile=open(iFile1)
    for line in inFile :
        row+=1
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        if k in dict1:
            if dict1[k].find('rs')==0 :
                dbsnp135+=1
            if dict2[k].find('rs')==0 :
                dbsnp132+=1
    inFile.close()
    print(iFile1+'\t'+str(row)+'\t'+str(dbsnp132)+'(%4.2f%%)'%(dbsnp132/float(row)*100))+'\t'+str(dbsnp135)+'(%4.2f%%)'%(dbsnp135/float(row)*100)

somatic_cmp_dbsnp('SNV.genome.ICC4A','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC5A','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC9A','sum_snp.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC10A','sum_snp.genome_summary.012')
#
somatic_cmp_dbsnp('SNV.genome.ICC4B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC5B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC9B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.ICC10B','sum_snp34.genome_summary.012')
##
somatic_cmp_dbsnp('SNV.genome.CHC5A','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC6A','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC7A','sum_snp2.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC10A','sum_snp2.genome_summary.012')
##
somatic_cmp_dbsnp('SNV.genome.CHC5B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC6B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC7B','sum_snp34.genome_summary.012')
somatic_cmp_dbsnp('SNV.genome.CHC10B','sum_snp34.genome_summary.012')
##
##
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

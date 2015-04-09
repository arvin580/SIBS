def somatic_cmp_dbsnp(iFile1,iFile2,oFile) :
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
    ouFile=open(oFile,'w')
    for line in inFile :
        row+=1
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if k in dict1:
            if dict1[k].find('rs')==0 :
                dbsnp135+=1
            else :
                ouFile.write(line+'\n')
            #if dict2[k].find('rs')==0 :
            #    dbsnp132+=1
    inFile.close()
    ouFile.close()
    #print(iFile1+'\t'+str(row)+'\t'+str(dbsnp132)+'(%4.2f%%)'%(dbsnp132/float(row)*100))+'\t'+str(dbsnp135)+'(%4.2f%%)'%(dbsnp135/float(row)*100)


somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.ICC4','sum_snp.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.ICC4.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.ICC5','sum_snp.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.ICC5.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.ICC9','sum_snp.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.ICC9.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.ICC10','sum_snp.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.ICC10.somatic_minus_dbsnp')

somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.CHC5','sum_snp2.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.CHC5.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.CHC6','sum_snp2.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.CHC6.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.CHC7','sum_snp2.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.CHC7.somatic_minus_dbsnp')
somatic_cmp_dbsnp('sum_snp.exome_summary.pass012.nonsynonymous.CHC10','sum_snp2.exome_summary.pass012','sum_snp.exome_summary.pass012.nonsynonymous.CHC10.somatic_minus_dbsnp')

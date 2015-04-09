def somatic_cmp_dbsnp(iFile1,iFile2) :
    dict1=dict()
    inFile=open(iFile2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        dict1[k]=fields[8]
    inFile.close()

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
    inFile.close()
    print(iFile1+'\t'+str(row)+'\t'+str(dbsnp135)+'(%4.2f%%)'%(dbsnp135/float(row)*100))

somatic_cmp_dbsnp('SNV.exome.ICC4A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC5A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC9A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC10A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
#
somatic_cmp_dbsnp('SNV.exome.ICC4B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC5B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC9B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.ICC10B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
##
somatic_cmp_dbsnp('SNV.exome.CHC5A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC6A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC7A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC10A.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
##
somatic_cmp_dbsnp('SNV.exome.CHC5B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC6B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC7B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.CHC10B.not.repeat','sum_snv16sExome.exome_summary.overall.filter')
##
##
somatic_cmp_dbsnp('SNV.exome.somatic.ICC4.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.ICC5.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.ICC9.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.ICC10.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
##
##
somatic_cmp_dbsnp('SNV.exome.somatic.CHC5.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.CHC6.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.CHC7.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')
somatic_cmp_dbsnp('SNV.exome.somatic.CHC10.not.repeat.mc','sum_snv16sExome.exome_summary.overall.filter')

def tumor_minus_normal_to_somatic(tumorFile,normalFile,oFile) :
    dict_Normal=dict()
    ouFile=open(oFile,'w')
    inFile=open(normalFile)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        dict_Normal[k]=1
    inFile.close()

    inFile=open(tumorFile)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        if k not in dict_Normal :
            ouFile.write(line+'\n')

    ouFile.close()




tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.ICC10A','sum_snp34.exome_summary.pass012.ICC10B','sum_snp.exome_summary.pass012.ICC10')
tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.ICC4A','sum_snp34.exome_summary.pass012.ICC4B','sum_snp.exome_summary.pass012.ICC4')
tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.ICC5A','sum_snp34.exome_summary.pass012.ICC5B','sum_snp.exome_summary.pass012.ICC5')
tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.ICC9A','sum_snp34.exome_summary.pass012.ICC9B','sum_snp.exome_summary.pass012.ICC9')


tumor_minus_normal_to_somatic('sum_snp2.exome_summary.pass012.CHC10A','sum_snp34.exome_summary.pass012.CHC10B','sum_snp.exome_summary.pass012.CHC10')
tumor_minus_normal_to_somatic('sum_snp2.exome_summary.pass012.CHC5A','sum_snp34.exome_summary.pass012.CHC5B','sum_snp.exome_summary.pass012.CHC5')
tumor_minus_normal_to_somatic('sum_snp2.exome_summary.pass012.CHC6A','sum_snp34.exome_summary.pass012.CHC6B','sum_snp.exome_summary.pass012.CHC6')
tumor_minus_normal_to_somatic('sum_snp2.exome_summary.pass012.CHC7A','sum_snp34.exome_summary.pass012.CHC7B','sum_snp.exome_summary.pass012.CHC7')

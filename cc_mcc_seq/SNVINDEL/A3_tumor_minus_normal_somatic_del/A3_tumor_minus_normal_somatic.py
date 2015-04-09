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




tumor_minus_normal_to_somatic('SNV.exome.ICC10A','SNV.exome.ICC10B','SNV.exome.somatic.ICC10')
tumor_minus_normal_to_somatic('SNV.exome.ICC4A','SNV.exome.ICC4B','SNV.exome.somatic.ICC4')
tumor_minus_normal_to_somatic('SNV.exome.ICC5A','SNV.exome.ICC5B','SNV.exome.somatic.ICC5')
tumor_minus_normal_to_somatic('SNV.exome.ICC9A','SNV.exome.ICC9B','SNV.exome.somatic.ICC9')


tumor_minus_normal_to_somatic('SNV.exome.CHC10A','SNV.exome.CHC10B','SNV.exome.somatic.CHC10')
tumor_minus_normal_to_somatic('SNV.exome.CHC5A','SNV.exome.CHC5B','SNV.exome.somatic.CHC5')
tumor_minus_normal_to_somatic('SNV.exome.CHC6A','SNV.exome.CHC6B','SNV.exome.somatic.CHC6')
tumor_minus_normal_to_somatic('SNV.exome.CHC7A','SNV.exome.CHC7B','SNV.exome.somatic.CHC7')


tumor_minus_normal_to_somatic('SNV.genome.ICC10A','SNV.genome.ICC10B','SNV.genome.somatic.ICC10')
tumor_minus_normal_to_somatic('SNV.genome.ICC4A','SNV.genome.ICC4B','SNV.genome.somatic.ICC4')
tumor_minus_normal_to_somatic('SNV.genome.ICC5A','SNV.genome.ICC5B','SNV.genome.somatic.ICC5')
tumor_minus_normal_to_somatic('SNV.genome.ICC9A','SNV.genome.ICC9B','SNV.genome.somatic.ICC9')


tumor_minus_normal_to_somatic('SNV.genome.CHC10A','SNV.genome.CHC10B','SNV.genome.somatic.CHC10')
tumor_minus_normal_to_somatic('SNV.genome.CHC5A','SNV.genome.CHC5B','SNV.genome.somatic.CHC5')
tumor_minus_normal_to_somatic('SNV.genome.CHC6A','SNV.genome.CHC6B','SNV.genome.somatic.CHC6')
tumor_minus_normal_to_somatic('SNV.genome.CHC7A','SNV.genome.CHC7B','SNV.genome.somatic.CHC7')

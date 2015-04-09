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




tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC10A','SNV.exome.nopass.ICC10B','SNV.exome.nopass.somatic.ICC10')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC4A','SNV.exome.nopass.ICC4B','SNV.exome.nopass.somatic.ICC4')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC5A','SNV.exome.nopass.ICC5B','SNV.exome.nopass.somatic.ICC5')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC9A','SNV.exome.nopass.ICC9B','SNV.exome.nopass.somatic.ICC9')


tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC10A','SNV.exome.nopass.CHC10B','SNV.exome.nopass.somatic.CHC10')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC5A','SNV.exome.nopass.CHC5B','SNV.exome.nopass.somatic.CHC5')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC6A','SNV.exome.nopass.CHC6B','SNV.exome.nopass.somatic.CHC6')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC7A','SNV.exome.nopass.CHC7B','SNV.exome.nopass.somatic.CHC7')


tumor_minus_normal_to_somatic('SNV.genome.nopass.ICC10A','SNV.genome.nopass.ICC10B','SNV.genome.nopass.somatic.ICC10')
tumor_minus_normal_to_somatic('SNV.genome.nopass.ICC4A','SNV.genome.nopass.ICC4B','SNV.genome.nopass.somatic.ICC4')
tumor_minus_normal_to_somatic('SNV.genome.nopass.ICC5A','SNV.genome.nopass.ICC5B','SNV.genome.nopass.somatic.ICC5')
tumor_minus_normal_to_somatic('SNV.genome.nopass.ICC9A','SNV.genome.nopass.ICC9B','SNV.genome.nopass.somatic.ICC9')


tumor_minus_normal_to_somatic('SNV.genome.nopass.CHC10A','SNV.genome.nopass.CHC10B','SNV.genome.nopass.somatic.CHC10')
tumor_minus_normal_to_somatic('SNV.genome.nopass.CHC5A','SNV.genome.nopass.CHC5B','SNV.genome.nopass.somatic.CHC5')
tumor_minus_normal_to_somatic('SNV.genome.nopass.CHC6A','SNV.genome.nopass.CHC6B','SNV.genome.nopass.somatic.CHC6')
tumor_minus_normal_to_somatic('SNV.genome.nopass.CHC7A','SNV.genome.nopass.CHC7B','SNV.genome.nopass.somatic.CHC7')

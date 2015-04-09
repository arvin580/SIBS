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


tumor_minus_normal_to_somatic('SNV.genome.ICC10A','SNV.genome.ICC10B','SNV.genome.ICC10A10B')
tumor_minus_normal_to_somatic('SNV.genome.ICC10A','SNV.genome.ICC4B','SNV.genome.ICC10A4B')
tumor_minus_normal_to_somatic('SNV.genome.ICC10A','SNV.genome.ICC5B','SNV.genome.ICC10A5B')
tumor_minus_normal_to_somatic('SNV.genome.ICC10A','SNV.genome.ICC9B','SNV.genome.ICC10A9B')

tumor_minus_normal_to_somatic('SNV.genome.ICC4A','SNV.genome.ICC4B','SNV.genome.ICC4A4B')
tumor_minus_normal_to_somatic('SNV.genome.ICC4A','SNV.genome.ICC5B','SNV.genome.ICC4A5B')
tumor_minus_normal_to_somatic('SNV.genome.ICC4A','SNV.genome.ICC9B','SNV.genome.ICC4A9B')
tumor_minus_normal_to_somatic('SNV.genome.ICC4A','SNV.genome.ICC10B','SNV.genome.ICC4A10B')

tumor_minus_normal_to_somatic('SNV.genome.ICC5A','SNV.genome.ICC5B','SNV.genome.ICC5A5B')
tumor_minus_normal_to_somatic('SNV.genome.ICC5A','SNV.genome.ICC4B','SNV.genome.ICC5A4B')
tumor_minus_normal_to_somatic('SNV.genome.ICC5A','SNV.genome.ICC9B','SNV.genome.ICC5A9B')
tumor_minus_normal_to_somatic('SNV.genome.ICC5A','SNV.genome.ICC10B','SNV.genome.ICC5A10B')

tumor_minus_normal_to_somatic('SNV.genome.ICC9A','SNV.genome.ICC9B','SNV.genome.ICC9A9B')
tumor_minus_normal_to_somatic('SNV.genome.ICC9A','SNV.genome.ICC4B','SNV.genome.ICC9A4B')
tumor_minus_normal_to_somatic('SNV.genome.ICC9A','SNV.genome.ICC5B','SNV.genome.ICC9A5B')
tumor_minus_normal_to_somatic('SNV.genome.ICC9A','SNV.genome.ICC10B','SNV.genome.ICC9A10B')


tumor_minus_normal_to_somatic('SNV.genome.CHC10A','SNV.genome.CHC10B','SNV.genome.CHC10A10B')
tumor_minus_normal_to_somatic('SNV.genome.CHC10A','SNV.genome.CHC5B','SNV.genome.CHC10A5B')
tumor_minus_normal_to_somatic('SNV.genome.CHC10A','SNV.genome.CHC6B','SNV.genome.CHC10A6B')
tumor_minus_normal_to_somatic('SNV.genome.CHC10A','SNV.genome.CHC7B','SNV.genome.CHC10A7B')

tumor_minus_normal_to_somatic('SNV.genome.CHC5A','SNV.genome.CHC5B','SNV.genome.CHC5A5B')
tumor_minus_normal_to_somatic('SNV.genome.CHC5A','SNV.genome.CHC6B','SNV.genome.CHC5A6B')
tumor_minus_normal_to_somatic('SNV.genome.CHC5A','SNV.genome.CHC7B','SNV.genome.CHC5A7B')
tumor_minus_normal_to_somatic('SNV.genome.CHC5A','SNV.genome.CHC10B','SNV.genome.CHC5A10B')

tumor_minus_normal_to_somatic('SNV.genome.CHC6A','SNV.genome.CHC6B','SNV.genome.CHC6A6B')
tumor_minus_normal_to_somatic('SNV.genome.CHC6A','SNV.genome.CHC5B','SNV.genome.CHC6A5B')
tumor_minus_normal_to_somatic('SNV.genome.CHC6A','SNV.genome.CHC7B','SNV.genome.CHC6A7B')
tumor_minus_normal_to_somatic('SNV.genome.CHC6A','SNV.genome.CHC10B','SNV.genome.CHC6A10B')

tumor_minus_normal_to_somatic('SNV.genome.CHC7A','SNV.genome.CHC7B','SNV.genome.CHC7A7B')
tumor_minus_normal_to_somatic('SNV.genome.CHC7A','SNV.genome.CHC5B','SNV.genome.CHC7A5B')
tumor_minus_normal_to_somatic('SNV.genome.CHC7A','SNV.genome.CHC6B','SNV.genome.CHC7A6B')
tumor_minus_normal_to_somatic('SNV.genome.CHC7A','SNV.genome.CHC10B','SNV.genome.CHC7A10B')

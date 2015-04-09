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




tumor_minus_normal_to_somatic('INDEL.exome.nopass.ICC10A','INDEL.exome.nopass.ICC10B','INDEL.exome.nopass.somatic.ICC10')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.ICC4A','INDEL.exome.nopass.ICC4B','INDEL.exome.nopass.somatic.ICC4')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.ICC5A','INDEL.exome.nopass.ICC5B','INDEL.exome.nopass.somatic.ICC5')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.ICC9A','INDEL.exome.nopass.ICC9B','INDEL.exome.nopass.somatic.ICC9')


tumor_minus_normal_to_somatic('INDEL.exome.nopass.CHC10A','INDEL.exome.nopass.CHC10B','INDEL.exome.nopass.somatic.CHC10')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.CHC5A','INDEL.exome.nopass.CHC5B','INDEL.exome.nopass.somatic.CHC5')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.CHC6A','INDEL.exome.nopass.CHC6B','INDEL.exome.nopass.somatic.CHC6')
tumor_minus_normal_to_somatic('INDEL.exome.nopass.CHC7A','INDEL.exome.nopass.CHC7B','INDEL.exome.nopass.somatic.CHC7')


tumor_minus_normal_to_somatic('INDEL.genome.nopass.ICC10A','INDEL.genome.nopass.ICC10B','INDEL.genome.nopass.somatic.ICC10')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.ICC4A','INDEL.genome.nopass.ICC4B','INDEL.genome.nopass.somatic.ICC4')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.ICC5A','INDEL.genome.nopass.ICC5B','INDEL.genome.nopass.somatic.ICC5')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.ICC9A','INDEL.genome.nopass.ICC9B','INDEL.genome.nopass.somatic.ICC9')


tumor_minus_normal_to_somatic('INDEL.genome.nopass.CHC10A','INDEL.genome.nopass.CHC10B','INDEL.genome.nopass.somatic.CHC10')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.CHC5A','INDEL.genome.nopass.CHC5B','INDEL.genome.nopass.somatic.CHC5')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.CHC6A','INDEL.genome.nopass.CHC6B','INDEL.genome.nopass.somatic.CHC6')
tumor_minus_normal_to_somatic('INDEL.genome.nopass.CHC7A','INDEL.genome.nopass.CHC7B','INDEL.genome.nopass.somatic.CHC7')

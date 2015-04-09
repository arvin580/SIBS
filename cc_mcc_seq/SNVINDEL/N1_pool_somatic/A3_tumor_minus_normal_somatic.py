def normal(inFList) :
    D=dict()
    for f in inFList :
        inFile=open(f)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            k='\t'.join(fields[1:-1])
            D[k]=1
        inFile.close()
    return D

inFList=['SNV.exome.nopass.ICC10B','SNV.exome.nopass.ICC4B','SNV.exome.nopass.ICC5B','SNV.exome.nopass.ICC9B'
        ,'SNV.exome.nopass.CHC10B','SNV.exome.nopass.CHC5B','SNV.exome.nopass.CHC6B','SNV.exome.nopass.CHC7B']
D=normal(inFList)


def tumor_minus_normal_to_somatic(tumorFile,oFile) :
    ouFile=open(oFile,'w')
    inFile=open(tumorFile)

    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        if k not in D :
            ouFile.write(line+'\n')

    ouFile.close()




tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC10A','SNV.exome.nopass.somatic.ICC10')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC4A','SNV.exome.nopass.somatic.ICC4')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC5A','SNV.exome.nopass.somatic.ICC5')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC9A','SNV.exome.nopass.somatic.ICC9')

tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC1A','SNV.exome.nopass.somatic.ICC1')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC2A','SNV.exome.nopass.somatic.ICC2')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC3A','SNV.exome.nopass.somatic.ICC3')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC6A','SNV.exome.nopass.somatic.ICC6')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC7A','SNV.exome.nopass.somatic.ICC7')
tumor_minus_normal_to_somatic('SNV.exome.nopass.ICC8A','SNV.exome.nopass.somatic.ICC8')

tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC10A','SNV.exome.nopass.somatic.CHC10')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC5A','SNV.exome.nopass.somatic.CHC5')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC6A','SNV.exome.nopass.somatic.CHC6')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC7A','SNV.exome.nopass.somatic.CHC7')

tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC1A','SNV.exome.nopass.somatic.CHC1')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC2A','SNV.exome.nopass.somatic.CHC2')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC3A','SNV.exome.nopass.somatic.CHC3')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC4A','SNV.exome.nopass.somatic.CHC4')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC8A','SNV.exome.nopass.somatic.CHC8')
tumor_minus_normal_to_somatic('SNV.exome.nopass.CHC9A','SNV.exome.nopass.somatic.CHC9')

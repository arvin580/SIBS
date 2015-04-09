def snv_indel(inF):
    inFile = open(inF)
    ouFile1 = open(inF.split('vcf')[0]+'snv'+'.vcf','w')
    ouFile2 = open(inF.split('vcf')[0]+'indel'+'.vcf','w')

    for line in inFile:
        fields = line.split('\t')
        if fields[7].find('INDEL')==0:
            ouFile2.write(line)
        else:
            ouFile1.write(line)
        
    inFile.close()
    ouFile1.close()
    ouFile2.close()

snv_indel('var.flt.vcf')

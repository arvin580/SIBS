def snv_number(inF,ouF):
    inFile = open(inF)
    ouFile = open(ouF,'a')
    snv = [0]*10
    for x in range(125):
        inFile.readline()
    for line in inFile:
        line = line.strip()
        fields =line.split('\t')
        for i,item in enumerate(fields[-10:]):
            if item .find('0/1')==0 or item.find('1/1')==0:
                snv[i]+=1
    for x in snv:
        ouFile.write(str(x)+'\t')

    inFile.close()
    ouFile.close()

snv_number('ICC.raw.snp.recalibrated.vcf','snv.gatk.number')
snv_number('CHC.raw.snp.recalibrated.vcf','snv.gatk.number')
snv_number('ICCCHC.raw.snp.recalibrated.vcf','snv.gatk.number')



def snv_number(inF,ouF):
    snv = [0]*17
    inFile = open(inF)
    ouFile = open(ouF,'w')
    for line in inFile:
        snv[16]+=1
        line = line.strip()
        fields =line.split('\t')
        for i,item in enumerate(fields[-16:]):
            if item .find('0/0')==-1 :
                if float(item.split(':')[-1]) > 20:
                    snv[i]+=1
    for x in snv:
        ouFile.write(str(x)+'\t')

    inFile.close()
    ouFile.close()

snv_number('var.flt.vcf','snv.samtools.filter.number')



inFile=open('raw.snp.recalibrated.vcf')
ouFile=open('raw.snp.recalibrated.vcf.qual','w')

list1=list()

for i in range(125) :
    inFile.readline()

for line in inFile :
    fields=line.split('\t')
    list1.append(fields[5])
inFile.close()


ouFile.write('\n'.join(list1))

ouFile.close()


import sys
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
                'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
                        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']
head = 27
ouFile = open('var.flt.vcf','w')
for ch in chrs:
    f = 'var.flt.%s.vcf'%ch 
    inFile=open(f)
    for n in range(head):
        line = inFile.readline()
    for line in inFile:
        ouFile.write(line)
    inFile.close()
ouFile.close()

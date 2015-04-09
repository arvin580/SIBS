import sys
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
                'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
                        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']
ouFile = open('1.depth','w')
for ch in chrs:
    f = '1.depth.%s'%ch 
    inFile=open(f)
    for line in inFile:
        ouFile.write(line)
    inFile.close()
ouFile.close()

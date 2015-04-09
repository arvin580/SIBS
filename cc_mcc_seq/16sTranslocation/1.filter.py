import sys
flags = [81,161,97,145,65,129,113,177]
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14',
        'chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.filtered', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if int(fields[1]) in flags and fields[2] in chrs:
        ouFile.write(line+'\n')
inFile.close()

ouFile.close()



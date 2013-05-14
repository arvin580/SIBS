import sys

chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
                'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
                        'chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']


def normal(inF):
    inFile = open(inF)
    ouFile = open(inF+'.normal', 'w')
    ouFile2 = open(inF+'.not-normal', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            if fields[3] in chrs and fields[15] in chrs:
                ouFile.write(line1+'\n')
                ouFile.write(line2+'\n')
            else:
                ouFile2.write(line1+'\n')
                ouFile2.write(line2+'\n')
        else:
            break

    inFile.close()
    ouFile.close()
    ouFile2.close()

normal('split-mapped-duplication')
normal('split-mapped-inversion')
normal('split-mapped-translocation')
normal('split-mapped-deletion')

### py cat.py varScan.CHC6 

chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
                'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
                        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']
import sys

ouFile = open(sys.argv[1] + '.copynumber.called', 'w')

for ch in chrs:
    inFile = open(sys.argv[1] + '.' + ch + '.copynumber.called')
    line = inFile.readline()
    #if ch =='chr1':
    #    ouFile.write(line)
    for line in inFile:
        ouFile.write(line)
    inFile.close()
ouFile.close()



import os
import sys 
head = 27
num = [0] * 16
somatic = [0] * 8 
for ch in ['chr22']:
    f = 'var.flt.%s.vcf'%ch
    inFile=open(f)
    for n in range(head):
        line = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i,item in enumerate(fields[-16:]):
            gq = item.split(':')[-1]
            if gq == '2':
                print(fields[1])
    inFile.close()



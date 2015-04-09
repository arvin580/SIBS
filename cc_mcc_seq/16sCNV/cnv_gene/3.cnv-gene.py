### python 3.cnv-gene.py varScan.CHC10.copynumber.called.depth 2

import sys
from read_chr_depth import *

upper = float(sys.argv[2])
down = 1 / float(sys.argv[2])

inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'_'+sys.argv[2]+'_upper_gene', 'w')
ouFile2 = open(sys.argv[1]+'_'+sys.argv[2]+'_down_gene', 'w')
ouFile3 = open(sys.argv[1]+'_'+sys.argv[2]+'_upped_down_gene', 'w')

chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
        'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16',
        'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22',
        'chrX', 'chrY']

sA = sys.argv[1].split('.')[1]+'A'
sB = sys.argv[1].split('.')[1]+'B'


D1= {}
D2= {}
D3= {}

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)==6:
        ch = fields[2].split(':')[0]
        if ch in chrs:
            if (float(fields[4])+1)/(float(fields[3])+1)*Depth[sB][ch]/Depth[sA][ch] > upper:
                D1[fields[0]+':'+fields[2]]=1
                D3[fields[0]+':'+fields[2]]=1
    
            elif (float(fields[4])+1)/(float(fields[3])+1)*Depth[sB][ch]/Depth[sA][ch] < down:
                D2[fields[0]+':'+fields[2]]=1
                D3[fields[0]+':'+fields[2]]=1

for k in D1:
    ouFile1.write(k+'\n')
for k in D2:
    ouFile2.write(k+'\n')
for k in D3:
    ouFile3.write(k+'\n')



ouFile1.close()
ouFile2.close()
ouFile3.close()
        


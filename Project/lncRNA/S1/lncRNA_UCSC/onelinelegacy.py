###  python oneline.py  lncrna_ucsc_human_mrna

import sys
dict1=dict()

inFile1=open(sys.argv[1],'r')

for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        head=line
        dict1[head]=[]
    else :
        dict1[head].append(line)

inFile1.close()

ouFile1=open(sys.argv[1]+'.fa','w')

for key in dict1 :
    ouFile1.write(key+'\n')
    ouFile1.write(''.join(dict1[key])+'\n')

ouFile1.close()

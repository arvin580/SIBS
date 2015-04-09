### python ctx.py /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt


import sys

inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.ctx','w')

for line in inFile1 :
    fields=line.split('\t')
    if fields[8]=='CTX':
        ouFile1.write(line)

inFile1.close()
ouFile1.close()

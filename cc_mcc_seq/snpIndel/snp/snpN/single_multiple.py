#!/usr/bin/python
### python single_multiple.py /netshare1/home1/szzhongxin/proj1/hansun/snpIndel/snp/snpN/tmp  /netshare1/home1/szzhongxin/proj1/hansun/snpIndel/snp/raw.snp.vcf single_multiple2.stat

import sys
import os
import re

inDir1=sys.argv[1]
inFile1=sys.argv[2]
ouFile1=sys.argv[3]

dict1={}
ouFileA=open(ouFile1,'w')

for file in os.listdir(inDir1) :
    if re.search(r'\.vcf$',file) :
        row=0;
        snp=0;
        inFile=open(inDir1+'/'+file,'r')
        while row<119 :
            line=inFile.readline()
            row+=1
        for line in inFile :
            fd=line.split('\t')
            dict1['\t'.join(fd[0:2])]=1
            snp+=1
        ouFileA.write('%d\t' % snp)
        inFile.close()
ouFileA.write('\n')

for key in dict1 :
    ouFileA.write('%s\n' % key)
ouFileA.close()

#dict2={}
#inFileA=open(inFile1,'r')
#snp=0
#row=0
#while row<119 :
#    line=inFileA.readline()
#    row+=1
#    for line in inFileA :
#        fd=line.split('\t')
#        dict2['\t'.join(fd[0:2])]=1
#        snp+=1
#print('%d\n' % snp)
#inFileA.close()
#for key in dict2 :
#    print('%s\n' % key)



## python cmp2.py  /netshare1/home1/szzhongxin/proj1/hansun/annotation/snpindel_snp3030_raw.snp.recalibrated.vcf hcc_validated

import sys

a=[]
b=[]

inFile1=open(sys.argv[1],'r')
inFile2=open(sys.argv[2],'r')

i=0
while i<125 :
    inFile1.readline()
    i+=1

for line in inFile1 :
    fields=line.split('\t')
    pos=fields[0]+'\t'+fields[1]
    a.append(pos)
 

    
for line in inFile2 :
    fields=line.split('\t')
    pos='chr'+fields[1]+'\t'+fields[3]
    b.append(pos)
 
inFile1.close()
inFile2.close()

sa=set(a)
sb=set(b)

ab=sa & sb 
print('\t'.join(list(ab)))




## python cmp.py  /netshare1/home1/szzhongxin/proj1/hansun/annotation/snpindel_snp3030/snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function.genelevel hcc_validated

import sys

a=[]
b=[]

inFile1=open(sys.argv[1],'r')
inFile2=open(sys.argv[2],'r')

for line in inFile1 :
    a.append(line.split('\t')[0])
    
for line in inFile2 :
    b.append(line.split('\t')[0])
 
inFile1.close()
inFile2.close()

sa=set(a)
sb=set(b)

ab=sa & sb 
print('\t'.join(list(ab)))




## python strand_type.py snpindel_snp3030_raw.snp.recalibrated.vcf

import sys

inFile1=open(sys.argv[1],'r')

dict1=dict()

for line in inFile1 :
    fields=line.split()
    if len(fields)>6 :
        if fields[6]=='PASS' and fields[2]=='.' :
            dict1.setdefault(fields[3]+fields[4],0)
            dict1[fields[3]+fields[4]]+=1
inFile1.close()
for item in sorted(dict1.items(),key=lambda x:x[1],reverse=True) :
    print(item[0]+'\t'+str(item[1])+'\n')

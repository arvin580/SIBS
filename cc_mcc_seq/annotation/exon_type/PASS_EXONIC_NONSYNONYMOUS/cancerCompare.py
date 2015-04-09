### python cancerCompare.py  snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV
### python cancerCompare.py  snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_dbsnp_nonsynonymous_SNV snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_dbsnp_nonsynonymous_SNV


import sys
import os

inFile1=open(sys.argv[1],'r')
inFile2=open(sys.argv[2],'r')

set1=set()
set2=set()

for line in inFile1 :
    fields=line.split('\t')
    set1.add(fields[3]+'\t'+fields[4])

for line in inFile2 :
    fields=line.split('\t')
    set2.add(fields[3]+'\t'+fields[4])

inFile1.close()
inFile2.close()

print(len(set1 & set2))
print(len(set1 - set2))
print(len(set2 - set1))

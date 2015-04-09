### python samplePlot.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV

import sys
import os

inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.plot','w')
row=0
for line in inFile1 :
    row+=1
    col=0
    fields=line.split('\t')
    for item in fields[17:25] :
        col+=1
        if item.find('0/1')==0 or item.find('1/1')==0 :
            ouFile1.write(str(col)+'\t'+str(row)+'\n')
ouFile1.close()
inFile1.close()

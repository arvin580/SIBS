### python heatmap.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV
### python heatmap.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_dbsnp_nonsynonymous_SNV
### python heatmap.py snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV
### python heatmap.py snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_dbsnp_nonsynonymous_SNV

import sys
import os

inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.heatmap','w')
for line in inFile1 :
    fields=line.split('\t')
    for item in fields[17:25] :
        if item.find('0/1')==0 or item.find('1/1')==0 :
            ouFile1.write('1'+'\t')
        else :
            ouFile1.write('0'+'\t')
    ouFile1.write('\n')
ouFile1.close()
inFile1.close()

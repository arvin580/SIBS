inFile1=open('snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function','r')
ouFile1=open('snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function.sift','w')
import re

for line in inFile1 :
    fields=line.split('\t')
    if fields[14]=='PASS' and fields[1]=='nonsynonymous SNV' and fields[10]=='.':
        s=re.search(r'^chr([\dxy][\dxy]?)$',fields[3])
        if s :
            chr=s.group(1)
            pos=fields[4]
            strand='1'
            geno=fields[6]+'/'+fields[7]
            ouFile1.write(chr+'\t'+pos+'\t'+strand+'\t'+geno+'\n')
        
inFile1.close()
ouFile1.close()

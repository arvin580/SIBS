#### python  sampleDistribution2.py  snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.distribution
#### python  sampleDistribution2.py  snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.distribution

import sys
import os
len=20

inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')

#dict1={}
#for line in inFile1 :
#    line=line.strip()
#    if line.find('>')==0 :
#        title=line
#        title=title.strip('>')
#        dict1[title]=[]
#    else :  
#        dict1[title].append(line)
#inFile1.close()
#
#for key in dict1 : 
#    dict1[key]=''.join(dict1[key])


inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.excel','w')
ouFile1.write('no.sample\tmutation type\tgene symbol\tchrom\tposition\tREF\tALT\tquality score\t1A\t2A\t3A\t4A\t5A\t6A\t7A\t8A\t9A\t10A\n')

for line in inFile1 :
    line=line.strip()
    fields=line.split('\t')
    gene=fields[3].split(':')[0]
    ouFile1.write(fields[0]+'\t'+fields[2]+'\t'+gene+'\t'+fields[4]+'\t'+fields[6]+'\t'+fields[7]+'\t'+fields[8]+'\t'+fields[14]+'\t')
    for item in fields[19:28] :
        sample=0
        if item.find('0/1')==0 or item.find('1/1')==0 :
            sample=1
        ouFile1.write(str(sample)+'\t')
    sample=0
    item=fields[18]
    if item.find('0/1')==0 or item.find('1/1')==0 :
        sample=1
    ouFile1.write(str(sample)+'\t') 
    ouFile1.write('\n')








inFile1.close()
ouFile1.close()

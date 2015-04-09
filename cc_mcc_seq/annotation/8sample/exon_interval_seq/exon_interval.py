### python exon_interval.py  ../snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function ../snpindel_indel3030_raw.indel.recalibrated.annovar.exonic_variant_function ../snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function ../snpindel2_indel3030_raw.indel.recalibrated.annovar.exonic_variant_function   15
import sys
import os

inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')

dict1={}
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        dict1[title]=[]
    else :  
        dict1[title].append(line)
inFile1.close()

for key in dict1 :
    dict1[key]=''.join(dict1[key])

for i in range(1,5) :

    inFile1=open(sys.argv[i],'r')
    ouFile1=open(os.path.basename(sys.argv[i])+'.intervals','w')
    
    for line in inFile1 :
        fields = line.split('\t')
        interval1 = int(fields[9])-int(sys.argv[5])
        interval2 = int(fields[9])+int(sys.argv[5])
        ouFile1.write('>'+fields[8]+':'+str(interval1)+':'+str(interval2)+'\n')
        ouFile1.write(dict1[fields[8]][interval1-1:interval2]+'\n')
    
    
    
    inFile1.close()
    ouFile1.close()

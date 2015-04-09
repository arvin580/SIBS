### python exontype.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function
### python exontype.py snpindel_indel3030_raw.indel.recalibrated.annovar.exonic_variant_function
### python exontype.py snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function
### python exontype.py snpindel2_indel3030_raw.indel.recalibrated.annovar.exonic_variant_function
import sys
import os
import re
inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.stat','w')

dict1={}
for line in inFile1:
    fields=line.split('\t')
    dict1.setdefault(fields[14],0)
    dict1[fields[14]]+=1
inFile1.close()

for key in dict1 :
    dict2={}
    dict3={}
    new=0
    dbsnp=0
    ouFile1.write(key+'\t'+str(dict1[key])+'\n')
    inFile1=open(sys.argv[1],'r')
    for line in inFile1:
        fields=line.split('\t')
        if fields[14] == key :
            if fields[10] == '.' :
                dict2.setdefault(fields[1],0)
                dict2[fields[1]]+=1
            elif fields[10].find('rs')==0 :
                dict3.setdefault(fields[1],0)
                dict3[fields[1]]+=1
    inFile1.close()

    for k in dict2 :
        new+=dict2[k]
    ouFile1.write('\tnew\t'+str(new)+'\n')
    for k in dict2 :
        ouFile1.write('\t\t'+k+'\t'+str(dict2[k])+'\n')
 
    for k in dict3 :
        dbsnp+=dict3[k]
    ouFile1.write('\tdbsnp\t'+str(dbsnp)+'\n')
    for k in dict3 :
        ouFile1.write('\t\t'+k+'\t'+str(dict3[k])+'\n')

ouFile1.close()

#### python distribution.py snpindel_snp3030_raw.snp.recalibrated.annovar.variant_function
#### python distribution.py snpindel_indel3030_raw.indel.recalibrated.annovar.variant_function
#### python distribution.py snpindel2_snp3030_raw.snp.recalibrated.annovar.variant_function
#### python distribution.py snpindel2_indel3030_raw.indel.recalibrated.annovar.variant_function
import sys
import os
import re
inFile1=open(sys.argv[1],'r')
ouFile1=open('%s.stat'%sys.argv[1],'w')

dict1={}
for line in inFile1:
    fields=line.split('\t')
    dict1.setdefault(fields[13],0)
    dict1[fields[13]]+=1
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
        if fields[13] == key :
            if fields[9] == '.' :
                dict2.setdefault(fields[0],0)
                dict2[fields[0]]+=1
            elif fields[9].find('rs')==0 :
                dict3.setdefault(fields[0],0)
                dict3[fields[0]]+=1
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

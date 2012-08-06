###  python filter.py  fusion_peptide_symbol fusion_point_3_2_complete_c_title_symbol 
###  python filter.py  splicing_peptide_symbol splicing_point_3_2_complete_c_title_symbol 

import sys
import os

dict1=dict()
inFile1=open(sys.argv[2],'r')

for line in inFile1 :
    line=line.strip()
    fields=line.split()
    dict1[fields[0]+'\t'+fields[1]]=fields[2:6]
inFile1.close()


inFile2=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'_cancer','w')

for line in inFile2 :
    line=line.strip()
    fields=line.split()
    ouFile1.write(line+'\t'+'\t'.join(dict1[fields[0]+'\t'+fields[1]])+'\n')
inFile2.close()
ouFile1.close()

####  python pep2sym.py fusion_point_3_2_complete_c_title  fusion_peptide_mapnomap2_c fusion_peptide_symbol
####  python pep2sym.py splicing_point_3_2_complete_c_title  splicing_peptide_mapnomap2_c splicing_peptide_symbol
import sys
import os

dict1=dict()

inFile1=open(sys.argv[1],'r')

while True :
    line1=inFile1.readline()
    line1=line1.strip()
    line2=inFile1.readline()
    line2=line2.strip()
    if len(line1)==0 :
        break
    else :
        dict1[line1]=line2

inFile1.close()

inFile1=open(sys.argv[2],'r')
ouFile1=open(sys.argv[3],'w')

for line in inFile1 :
    line=line.strip()
    symline=dict1['#'+line]
    sym=':'.join(symline.split(':')[1:3])
    ouFile1.write(sym+'\t'+line+'\n')
inFile1.close()
ouFile1.close()

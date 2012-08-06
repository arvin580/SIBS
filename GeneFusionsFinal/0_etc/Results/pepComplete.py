
####   python pepComplete.py fusion_point_3_2_complete_c  fusion_peptide_symbol  fusion_peptide_symbol_complete
####   python pepComplete.py splicing_point_3_2_complete_c  splicing_peptide_symbol  splicing_peptide_symbol_complete
import sys
import os

inFile1=open(sys.argv[1],'r')
dict1=dict()
while True :
    line=inFile1.readline().strip()
    if len(line)==0 :
        break
    else :
        if line.find('#')==0 :
            line2=inFile1.readline()
            line3=inFile1.readline()
            line3=line3.strip()
            dict1[line.strip('#')]=line3

inFile1.close()

inFile2=open(sys.argv[2],'r')
ouFile1=open(sys.argv[3],'w')

for line in inFile2 :
    line=line.strip()
    fields=line.split()
    ouFile1.write(line+'\t'+dict1[fields[1]]+'\n')

inFile2.close()
ouFile1.close()

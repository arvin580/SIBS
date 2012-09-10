### python spectrum_peptide3.py fusion_spectrum_peptide_mapnomap2 fusion_point_3_2_complete_c_title_x >fusion_spectrum_peptide_mapnomap2_symbol
### python spectrum_peptide3.py splicing_spectrum_peptide_mapnomap2 splicing_point_3_2_complete_c_title_x >splicing_spectrum_peptide_mapnomap2_symbol
import sys
import os
import re

inFile1=open(sys.argv[2])

dict1={}

while True :
    line1=inFile1.readline()
    line2=inFile1.readline()
    if len(line1)==0 :
        break
    else :
        pep=line1.strip('#\n')
        fd=line2.split(':')
        sym=':'.join(fd[1:3])
        dict1[pep]=sym

inFile1.close()


inFile1=open(sys.argv[1])
for line in inFile1 :
    pep=line.split()
    print(pep[0]+'\t'+dict1[pep[0]]+'\t'+'\t'.join(pep[1:]))
inFile1.close()

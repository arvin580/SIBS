#!/usr/bin/python

### python spectrum_peptide2.py fusion_point_3_2_complete_c_title spectrum_peptide_map spectrum_peptide_map2 fusion_spectrum_peptide_mapnomap2 fusion_spectrum_peptide_mapandmap
### python spectrum_peptide2.py splicing_point_3_2_complete_c_title spectrum_peptide_map spectrum_peptide_map2 splicing_spectrum_peptide_mapnomap2 splicing_spectrum_peptide_mapandmap


import os
import sys
import re

dict1={}
dict2={}
inFile1=open(sys.argv[2],'r')
for line in inFile1 :
    fd=line.split()
    dict1[fd[0]]=fd[1:]
inFile1.close()

inFile1=open(sys.argv[3],'r')
for line in inFile1 :
    fd=line.split()
    dict2[fd[0]]=fd[1:]
inFile1.close()


inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[4],'w')
ouFile2=open(sys.argv[5],'w')


for line in inFile1 :
    spec1=[]
    spec2=[]
    fd=line.split()
    for key in dict1 :
        if fd[0] in dict1[key] :
            spec1.append(key)
            if key in dict2 :
                spec2.append(key)
    if len(spec2)==0 :
        ouFile1.write(fd[0]+'\t')
        ouFile1.write('\t'.join(spec1))
        ouFile1.write('\n')
    else :
        spec1_set=set(spec1)
        spec2_set=set(spec2)
        ouFile2.write(fd[0]+'\n')
        ouFile2.write('\t'.join(list(spec1_set - spec2_set))+'\n')
        ouFile2.write('\t'.join(list(spec1_set & spec2_set))+'\n')


inFile1.close()
ouFile1.close()
ouFile2.close()



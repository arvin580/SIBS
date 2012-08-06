### python id_mapping2.py hg19_refGene.txt A_small_cell_lung_cancer_genome_with_complex_signatures_of_tobacco_exposure_nature08629-s4.txt
import sys
import os
import re

dict1={}
inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[2]+'.fusiongene','w')
for line in inFile1 :
    fields=line.split('\t')
    dict1[fields[1]]=[]
    dict1[fields[1]].append(fields[12])
    dict1[fields[1]].append(fields[2])
    dict1[fields[1]].append(fields[3])
    dict1[fields[1]].append(fields[4])
    dict1[fields[1]].append(fields[5])
inFile1.close()

#for key in dict1 :
#    print(key+'\t'+'\t'.join(dict1[key]))

inFile2=open(sys.argv[2],'r')

for line in inFile2 :
    fields=line.split('\t')
    head='###'
    tail='###'
    for key in dict1 :
        if dict1[key][1]==('chr'+fields[3]) and int(dict1[key][3])<=int(fields[4])<=int(dict1[key][4])  :
            head=dict1[key][0]

    for key in dict1 :
        if dict1[key][1]==('chr'+fields[6]) and int(dict1[key][3])<=int(fields[7])<=int(dict1[key][4])  :
            tail=dict1[key][0]
    ouFile1.write(head+'\t'+tail+'\n')

inFile2.close()
ouFile1.close()



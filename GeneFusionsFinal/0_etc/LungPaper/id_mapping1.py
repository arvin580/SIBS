### python id_mapping1.py hg19_refGene.txt The_mutation_spectrum_revealed_by_paired_genome_sequences_from_a_lung_cancer_patient_nature09004-s2.txt 
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
    if fields[5]!='NA' :
        if fields[5] in dict1 :
            head=dict1[fields[5]][0]
        else :
            if dict1[key][1]==fields[1] and (int(dict1[key][3])<=int(fields[2])<=int(dict1[key][4]) or int(dict1[key][3])<=int(fields[3])<=int(dict1[key][4])) :
                head=dict1[key][0]
    else :
        for key in dict1 :
            if dict1[key][1]==fields[1] and (int(dict1[key][3])<=int(fields[2])<=int(dict1[key][4]) or int(dict1[key][3])<=int(fields[3])<=int(dict1[key][4])) :
                head=dict1[key][0]

    if fields[11]!='NA' :
        if fields[11] in dict1 :
            tail=dict1[fields[11]][0]
        else :
            if dict1[key][1]==fields[7] and (int(dict1[key][3])<=int(fields[8])<=int(dict1[key][4]) or int(dict1[key][3])<=int(fields[9])<=int(dict1[key][4])) :
                 tail=dict1[key][0]
    else :
        for key in dict1 :
            if dict1[key][1]==fields[7] and (int(dict1[key][3])<=int(fields[8])<=int(dict1[key][4]) or int(dict1[key][3])<=int(fields[9])<=int(dict1[key][4])) :
                tail=dict1[key][0]
    ouFile1.write(head+'\t'+tail+'\n')

inFile2.close()
ouFile1.close()


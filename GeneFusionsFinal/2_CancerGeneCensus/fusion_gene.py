### python fusion_gene.py CancerGeneCensus_Table_1_full_2011-11-15.txt >fusion_gene_unique_CancerGeneCensus

import sys
import os
inFile1=open(sys.argv[1],'r')

dict1={}
for line in inFile1:
    fields=line.split('\t')
    head=fields[0].split(',')
    tail=fields[13].split(',')
    for val1 in head :
        for val2 in tail :
            v1=val1.strip(' "')
            v2=val2.strip(' "')
            if v1!='' and v2!='' :
                key1=v1+'\t'+v2
                key2=v2+'\t'+v1
                if key1 in dict1 or key2 in dict1:
                    if  key1 in dict1 :
                        dict1.setdefault(key1,0)
                        dict1[key1]+=1
    
                    if  key2 in dict1 :
                        dict1.setdefault(key2,0)
                        dict1[key2]+=1
    
                else :
    
                        dict1.setdefault(key1,0)
                        dict1[key1]+=1

inFile1.close()

for key in dict1 :
    print(key)


### python fusion_gene_unique_mapped.py fusion_gene_unique_chimerdb_mapped
import os
import sys
inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.stat','w')
dict1={}
for line in inFile1:
    fields=line.split()
    dict1.setdefault(fields[0],0)
    dict1.setdefault(fields[1],0)
    dict1[fields[0]]+=1
    dict1[fields[1]]+=1
inFile1.close()

for key in dict1 :
    ouFile1.write(key+'\n')
ouFile1.close()


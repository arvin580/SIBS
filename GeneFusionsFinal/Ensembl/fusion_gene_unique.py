### python fusion_gene_unique.py fusion_gene_unique_chimerdb_mapped fusion_gene_unique_CancerGeneCensus_mapped  fusion_gene_unique_CancerGeneCensus_unmapped_c fusion_gene_unique_paper fusion_gene_unique
import sys

inFile1=open(sys.argv[1],'r')
inFile2=open(sys.argv[2],'r')
inFile3=open(sys.argv[3],'r')
inFile4=open(sys.argv[4],'r')
ouFile1=open(sys.argv[5],'w')

dict1={}
for line in inFile1 :
    fields=line.split()
    key1=fields[0]+'\t'+fields[1]
    key2=fields[1]+'\t'+fields[0]
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
for line in inFile2 :
    fields=line.split()
    key1=fields[0]+'\t'+fields[1]
    key2=fields[1]+'\t'+fields[0]
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
        print(key1)

for line in inFile3 :
    fields=line.split()
    key1=fields[0]+'\t'+fields[1]
    key2=fields[1]+'\t'+fields[0]
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
        print(key1)

for line in inFile4 :
    fields=line.split()
    key1=fields[0]+'\t'+fields[1]
    key2=fields[1]+'\t'+fields[0]
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
        print(key1)


for key in dict1 :
    ouFile1.write(key+'\n')



inFile1.close()
inFile2.close()
inFile3.close()
inFile4.close()
ouFile1.close()




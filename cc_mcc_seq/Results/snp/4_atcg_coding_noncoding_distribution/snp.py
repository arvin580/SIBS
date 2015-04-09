###  manual  excel

import os
os.chdir('genome')


inFile=open('sum_snp.genome_combined.sorted.pass012.new.atcg')

list1=list()

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    list1.append(fields)

inFile.close()

ouFile=open('sum_snp.genome_combined.sorted.pass012.new.atcg.genome2','w')

####exonic

type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)

for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(0,3) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write('exonic\t'+key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

####intronic
type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)


for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(3,4) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write('intronic\t'+key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

####UTR
type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)




for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(4,7) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write('UTR\t'+key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

#### ncRNA

type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)


for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(10,16) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write('ncRNA\t'+key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

#### intergenic
type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)

for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(16,17) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write('intergenic\t'+key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')



ouFile.close()


import os
os.chdir('genome')

inFile=open('sum_snp.genome_combined.sorted.pass012.known.atcg')

list1=list()

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    list1.append(fields)

inFile.close()

ouFile=open('sum_snp.genome_combined.sorted.pass012.known.atcg.genome','w')

type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)

for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(len(list1)) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()




list1=list1[0:3]

ouFile=open('sum_snp.genome_combined.sorted.pass012.known.atcg.exome','w')

type=[]
dict1=dict()
for i in range(4,280,23) :
    type.append(list1[0][i])
    dict1.setdefault(list1[0][i],[0]*20)

for i,item in enumerate(type) :
    for j in range(20) :
        for k in range(len(list1)) :
            dict1[item][j]+=int(list1[k][i*23+7+j])


for key in type :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()

import os
os.chdir('exome')



dict1=dict()
dict2=dict()

inFile=open('sum_indel.exome_combined.sorted.pass012.known')
ouFile=open('sum_indel.exome_combined.sorted.pass012.known.stat','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    type=fields[2]
    dict1.setdefault(type,[0]*23)

    for i,item in enumerate(fields[-20:]) :
        if int(item)>0 :
            dict1[type][i+3]+=1
    if sum([int(i) for i in fields[-20:-10]])>0 :
        dict1[type][1]+=1
    if sum([int(i) for i in fields[-10:]])>0 :
        dict1[type][2]+=1
    if sum([int(i) for i in fields[-20:]])>0 :
        dict1[type][0]+=1


inFile.close()

for key in dict1 :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()

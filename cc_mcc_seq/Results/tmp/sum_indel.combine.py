dict1=dict()
inFile=open('sum_indel.exome_summary.csv')
inFile.readline()
for line in inFile :
    line=line.strip()
    fields=line.split(',')
    print(len(fields))
    key=fields[0:31]
    key=','.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][0:14]=fields[31:]

inFile.close()

inFile=open('sum_indel2.exome_summary.csv')
head=inFile.readline()
for line in inFile :
    line=line.strip()
    fields=line.split(',')
    print(len(fields))
    key=fields[0:31]
    key=','.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][14:]=fields[31:]

inFile.close()

ouFile=open('sum_indel.exome_combined.csv','w')

ouFile.write(head)
for key in dict1 :
    ouFile.write(key+','+','.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()



'''
inFile=open('sum_indel.exome_summary.csv')
for line in inFile :
    line=line.strip()
    fields=line.split(',')
    flag=0
    for i,item in enum(list1) :
        if  fields[]==item[] :
            list1[i].append()
            flag=1
            continue
        if flag==0 :




inFile.close()
'''

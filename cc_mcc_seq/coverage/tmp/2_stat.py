inFile=open('fudan1.coverage.sample_statistics_dongxiao')
ouFile=open('fudan1.coverage.sample_statistics_dongxiao2','w')

list1=list()
for line  in inFile :
    line=line.strip()
    fields=line.split('\t')
    list1.append(fields)


inFile.close()

for i in range(len(fields)) :
    for j in range(len(list1)) :
        ouFile.write(list1[j][i]+'\t')
    ouFile.write('\n')

ouFile.close()

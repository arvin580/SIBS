import sys
D = {}
inFile = open(sys.argv[1])
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], [])
    D[fields[0]].append(line)
inFile.close()

ouFile = open(sys.argv[1]+'.stopgain.sorted', 'w')
d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)

#for item in d:
#    for it in item[1]:
#        ouFile.write(it + '\n')
for item in d:
    d = item[1]
    flag = 0
    for x in d:
        if x.find('StopGain')!=-1:
            flag += 1
    if flag:
        d.sort(cmp=lambda x,y:cmp(int((x.split('\t')[1].split(':')[-2])),int(y.split('\t')[1].split(':')[-2])))
        for it in d:
            ouFile.write(it + '\n')


ouFile.close()




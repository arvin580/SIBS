import sys
import re
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.gene', 'w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    if len(fields) >3:
        D.setdefault(fields[-1], 0)
        D[fields[-1]]+=1

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]), reverse = True)
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')

ouFile.close()

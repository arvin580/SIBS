import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.num','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[1],{})
    D[fields[1]][fields[0]] = 1
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])), reverse=True)
for item in d : 
    ouFile.write(item[0]+'\t'+str(len(item[1]))+'\n')

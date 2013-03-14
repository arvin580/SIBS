D = {}
inFile = open('split-mapped-duplication.gene.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], 0)
    D[fields[0]]=+1
inFile.close()

inFile = open('split-mapped-inversion.gene.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], 0)
    D[fields[0]]=+1
inFile.close()

inFile = open('split-mapped-translocation.gene.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], 0)
    D[fields[0]]=+1
inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(x,y), reverse = True)

for item in d:
    print(item[0]+'\t'+str(item[1]))

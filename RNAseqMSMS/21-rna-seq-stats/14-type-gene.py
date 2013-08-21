D = {}
inFile = open('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_one.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], 0)
    D[fields[0]] += 1
inFile.close()

inFile = open('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_one.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], 0)
    D[fields[0]] += 1
inFile.close()

inFile = open('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_one.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], 0)
    D[fields[0]] += 1
inFile.close()

inFile = open('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_one.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], 0)
    D[fields[0]] += 1
inFile.close()



d = D.items()
d.sort(cmp = lambda x,y:cmp(x[1],y[1]), reverse = True)

ouFile = open('split-mapped-deletion-inversion-duplication-translocation.gene','w')
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')

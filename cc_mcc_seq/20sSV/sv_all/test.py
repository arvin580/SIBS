inFile = open('delly.1.sv.stat.gene.symbol')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[1:]:
        D.setdefault(item,0)
        D[item]+=1
inFile.close()
for x in D:
    if D[x]>2:
        print(x+'\t'+str(D[x]))

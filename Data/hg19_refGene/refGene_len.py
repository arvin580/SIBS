D = {}
inFile = open('refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    length = int(fields[5]) - int(fields[4])
    D.setdefault(length,[])
    D[length].append(line)
inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(x[0],y[0]))
for item in d:
    print(str(item[0])+'\t'+'\t'.join(item[1]))

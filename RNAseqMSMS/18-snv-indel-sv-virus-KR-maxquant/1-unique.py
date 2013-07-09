inFile = open('evidence.txt')
ouFile = open('evidence-unique','w')
inFile.readline()
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split()
    pep = fields[0]
    D.setdefault(pep,[])
    D[pep].append(line)
inFile.close()

for k in D:
    ouFile.write('\t'.join(D[k])+'\n')
ouFile.close()

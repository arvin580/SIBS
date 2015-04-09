inFile = open('CHC10B.jmp.sam.unique.paired.sorted')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0] + '\t' + fields[1], 0)
    D[fields[0] + '\t' + fields[1]] += 1
inFile.close()
for k in D:
    print(k + '\t' +str(D[k]))

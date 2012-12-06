import sys
inFile = open(sys.argv[1])
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0] + ':' + fields[1]
    D.setdefault(k, 0)
    D[k] += 1
inFile.close()

for k in D:
    print(k + '\t' + str(D[k]))

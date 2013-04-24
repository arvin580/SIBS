import sys

FDR = 0.01

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.fdr', 'w')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = line


d = D.items()
d.sort(cmp = cmp(x,y :lambda cmpfun(x,y)))


inFile.close()
ouFile.close()



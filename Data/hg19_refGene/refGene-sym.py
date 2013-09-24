inFile = open('refGene-2013-04-22.txt')
ouFile = open('hg19-refGene.sym','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[12]] = 1
inFile.close()

for k in D:
    ouFile.write(k+'\n')
ouFile.close()

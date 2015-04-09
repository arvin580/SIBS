inFile = open('1.sv.stat.gene')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[1:]:
        D[item]=1
inFile.close()
print(len(D))

inFile = open('1.sv.stat.gene.dbsnp2')
D2 = {}
for line in inFile:
    line = line.strip()
    if line.find('chr')==0:
        D2[line]=1
inFile.close()
print(len(D2))



inFile = open('1.sv.stat.gene.dbsnp')
D = {}
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D.setdefault(line1, [])
        D[line1].append(line2)
    else:
        break
        
inFile.close()

ouFile = open('1.sv.stat.gene.dbsnp2', 'w')
for k in D:
    for item in D[k]:
        fields = item.split('\t')
        if (int(fields[3]) - int(fields[2])) > 100 :
            ouFile.write(k+'\n')
            ouFile.write(item+'\n')

ouFile.close()

D = {}
inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New')
ouFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-num-maxquant', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    num = int(fields[2])
    D.setdefault(num, 0)
    D[num] += 1
inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(x[0],y[0]))
for k in d:
    ouFile.write(str(k[0]) + '\t' + str(k[1]) + '\n')
ouFile.close()

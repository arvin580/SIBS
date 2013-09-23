D1 = {}
D2 = {}

inFile = open('unmapped-blated-viruses-100-76.seq.gene-stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D1[fields[0]] = int(fields[1])
inFile.close()

inFile = open('unmapped-blated-viruses-90-60.seq.gene-stat')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2[fields[0]] = int(fields[1])
inFile.close()

print(D1['E1'])
print(D2['E1'])

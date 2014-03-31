D = {}

inFile = open('HeLa-peptide-Predicted-pep-New')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
    D.setdefault(pep, [])
    D[pep].append(line)
inFile.close()


inFile = open('HeLa-Peptide-Predicted-MaxQuant-pep-New')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[2]
    D.setdefault(pep, [])
    D[pep].append(line)
inFile.close()

ouFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New', 'w')

for k in D:
    if len(D[k]) == 2:
        ouFile.write(k + '\t' + '\t'.join(D[k])+ '\n')
ouFile.close()

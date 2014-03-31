D = {}
inFile = open('HeLa-Peptide-Validation-gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
    #geneid = fields[1].split(':')[0]
    D.setdefault(fields[1], [])
    D[fields[1]].append(pep)
inFile.close()

ouFile = open('HeLa-Peptide-Validation-gene-dist', 'w')
for k in D:
    ouFile.write(k + '\t' + str(len(D[k])) + '\t' + '\t'.join(D[k]) + '\n')

ouFile.close()

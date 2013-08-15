D = {}
inFile = open('protID.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0] + '\t' + fields[1]
    D[k] = 1
inFile.close()

inFile = open('PDB-blasted-seq.txt')
ouFile = open('PDB-blasted-seq-matched.txt', 'w')
ouFile2 = open('PDB-blasted-seq-not_matched.txt', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    s1 = fields[0]
    s2 = fields[1].split('|')[1]
    k = s1 + '\t' + s2
    if k in D:
        ouFile.write(line + '\n')
    else:
        ouFile2.write(line + '\n')
inFile.close()
ouFile.close()
ouFile2.close()



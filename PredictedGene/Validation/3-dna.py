D = {}
inFile = open('ERR0498-04-05-DNA')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split(':')
        dna = fields[1]
        D.setdefault(dna, [])
        D[dna].append(line2)
    else:
        break
inFile.close()

inFile = open('HeLa-Peptide-Validation.txt')
ouFile = open('HeLa-Peptide-Validation-RNA_Seq-Num', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    pep = fields[0]
    dna = fields[1]
    ouFile.write('>' + pep + '\t' + dna  + '\n')
    if dna in D:
        ouFile.write(str(len(D[dna])) + '\n')

inFile.close()
ouFile.close()

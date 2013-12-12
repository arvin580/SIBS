inFile = open('Identified-Peptides-Corresponding-Reads')
ouFile = open('Identified-Peptides-Corresponding-Reads2')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
inFile.close()
ouFile.close()

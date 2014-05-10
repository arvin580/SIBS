D = {}
inFile = open('HeLa-Peptide-Variant-MaxQuant-XTandem')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[7]] = line
inFile.close()

inFile = open('HeLa-Variant-Peptide')
ouFile = open('HeLa-Variant-Peptide-Validated2', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] in D:
        ouFile.write(D[fields[0]] + '\n')
    else:
        print(fields[0])
inFile.close()

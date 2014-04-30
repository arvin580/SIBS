D = {}
inFile = open('z')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[7]] = 1
inFile.close()

inFile = open('HeLa-Peptide-Variant')
for line in inFile:
    line = line.strip()
    if line not in D:
        print(line)
inFile.close()

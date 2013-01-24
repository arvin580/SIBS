inFile = open('3-stopgain-protein-unique2-filtered.blated.filtered.snv')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    print(int(fields[13]))
inFile.close()

inFile = open('3-stopgain-protein-unique2-filtered.blated')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if int(fields[8])>int(fields[9]):
        print(line)
inFile.close()

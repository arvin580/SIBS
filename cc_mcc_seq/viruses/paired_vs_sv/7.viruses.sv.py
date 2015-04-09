interval = 10000
inFile = open('viruses.paired.seq')
ouFile = open('viruses.jumpy.paired.seq', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    sample = fields[0]
    ch = fields[1]
    pos = int(fields[2])
    ouFile.write(line + '\t')

    inFile2 = open('jumpy.paired.seq')
    for line in inFile2:
        line = line.strip()
        fields = line.split()
        if fields[1] == ch and fields[0][0:-1] == sample[0:-1]  :
            if pos-interval<=int(fields[2])<=pos+interval:
                ouFile.write(line+'\t')
    ouFile.write('\n')

inFile.close()

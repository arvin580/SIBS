inFile = open('1.sv.stat.exon.reads')
for line in inFile:
    line = line.strip()
    if line.find('>')==0:
        print(line)
inFile.close()

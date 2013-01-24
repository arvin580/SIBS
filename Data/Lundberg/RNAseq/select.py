inFile = open('SRR040290.sam')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>10:

inFile.close()

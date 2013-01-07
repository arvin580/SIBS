inFile = open('Tandem.Omssa.Fusion.Splicing.gene.curate')
LD = []
geneList = []
pepList = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    LD.append([int(x) for x in fields[2:4]])
    geneList.append(fields[0])
    pepList.append(fields[1])
inFile.close()
for x in LD:
    print(x)
for x in geneList:
    print(x)
for x in pepList:
    print(x)

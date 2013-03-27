D = {}
inFile = open('tandem.peptides.refinement-no')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[2]]=1
inFile.close()

inFile = open('tandem.peptides.refinement-yes-unanticipated.cleavage-no')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[2] not in D:
        print(fields[2])
inFile.close()

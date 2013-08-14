D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    D[fields[3]] = 1
inFile.close()
print(len(D))

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[1] not in D:
        print(line)
inFile.close()


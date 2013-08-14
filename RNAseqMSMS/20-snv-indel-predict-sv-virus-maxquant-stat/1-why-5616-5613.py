D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    D[fields[3]] = 1
inFile.close()
print(len(D))

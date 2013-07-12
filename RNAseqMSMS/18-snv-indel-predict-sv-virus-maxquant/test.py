inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene')
D = {}
for line in inFile:
    fields = line.split('\t')
    D[fields[2]]=1
inFile.close()
for k in D:
    print(k)

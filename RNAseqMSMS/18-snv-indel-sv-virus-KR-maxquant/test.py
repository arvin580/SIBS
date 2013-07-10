inFile = open('HeLa-peptide-snv-indel-predict-virus-sv-gene')
D = {}
for line in inFile:
    fields = line.split('\t')
    D[fields[4]]=1
inFile.close()

inFile = open('ha')
for line in inFile:
    fields = line.split('\t')
    if fields[2] not in D:
        print(line)
inFile.close()

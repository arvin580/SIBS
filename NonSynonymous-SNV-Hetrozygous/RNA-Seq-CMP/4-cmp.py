inFile = open('Peptides-Identified-Second-unSpec-single_SNV.num')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] =1
inFile.close()

inFile = open('Peptides-Identified-Second-unSpec-maxquant-sequest.num')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] in D:
        print(line)
inFile.close()

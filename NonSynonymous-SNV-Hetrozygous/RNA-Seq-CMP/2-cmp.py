D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-pFind3')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[9]
    D[pep] = 1
inFile.close()

inFile = open('Peptides-Identified-Second-unSpec')
ouFile = open('Peptides-Identified-Second-unSpec-xtandem-pfind', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fileds = line2.split('\t')
        pep = line2
        if pep in D:
            ouFile.write(line1 + '\n')
            ouFile.write(line2 + '\n')
    else:
        break
inFile.close()
ouFile.close()

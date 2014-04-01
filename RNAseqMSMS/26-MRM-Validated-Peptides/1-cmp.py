D = {}
inFile = open('HeLa-MRM-Validated-Peptides-Part1')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
ouFile = open('HeLa-MRM-Validated-Peptides-Part1-info', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[7]
    if pep in D:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()

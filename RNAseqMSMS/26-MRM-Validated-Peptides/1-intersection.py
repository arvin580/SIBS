D = {}
inFile = open('HeLa-Peptide-Variant')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
ouFile = open('HeLa-Variant-Peptide-Validated', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[7] in D:
        ouFile.write(line + '\n')
inFile.close()

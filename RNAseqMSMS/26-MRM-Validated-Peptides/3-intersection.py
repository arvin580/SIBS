D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[7]] = line
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-pFind3-pFind-Trypsin')
ouFile = open('HeLa-Peptide-Variant-MaxQuant-XTandem', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[9] in D:
        ouFile.write(D[fields[9]] + '\n')
inFile.close()

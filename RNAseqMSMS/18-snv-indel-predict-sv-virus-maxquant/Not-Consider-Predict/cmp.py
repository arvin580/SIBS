inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
D = {}
for line in inFile:
    fields = line.split('\t')
    D[fields[7]] = 0
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-NEW-sequest')
for line in inFile:
    fields = line.split('\t')
    if fields[7] not in D:
        print(line)
inFile.close()

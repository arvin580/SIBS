inFile = open('../12-maxuqant-sequest/HeLa-Peptide-Variant-Maxquant-Sequest-new')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[14]
    D[pep]=1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-spec')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-spec-sequest','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
    if pep in D:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()

inFile = open('../12-maxuqant-sequest/HeLa-Peptide-Predict-Maxquant-Sequest-new')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[14]
    D[pep]=1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-spec')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-spec-sequest','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
    if pep in D:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()

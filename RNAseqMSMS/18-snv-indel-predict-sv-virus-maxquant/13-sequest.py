inFile = open('12-maxuqant-sequest/HeLa-Peptide-Variant-Maxquant-Sequest-new')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[14]
    D[pep]=1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest','w')
ouFile2 = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest_total','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[6]
    if pep in D:
        ouFile.write('SEQUEST' + '\t'+line + '\n')
        ouFile2.write('SEQUEST' + '\t'+line + '\n')
    else:
        ouFile2.write('' + '\t'+line + '\n')
inFile.close()
ouFile.close()
ouFile2.close()

inFile = open('12-maxuqant-sequest/HeLa-Peptide-Predict-Maxquant-Sequest-new')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[14]
    D[pep]=1
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest','w')
ouFile2 = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest_total','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[6]
    if pep in D:
        ouFile.write('SEQUEST' + '\t'+line + '\n')
        ouFile2.write('SEQUEST' + '\t'+line + '\n')
    else:
        ouFile2.write('' + '\t'+line + '\n')
inFile.close()
ouFile.close()
ouFile2.close()

D = {}

inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[0]
    D[pep] = line
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest')
ouFile2 = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest-non-tandem', 'w')
ouFile1 = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest-tandem', 'w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[7]
    if pep in D:
        ouFile1.write(line + '\n')
    else:
        ouFile2.write(pep+'\n')
inFile.close()
ouFile1.close()
ouFile2.close()


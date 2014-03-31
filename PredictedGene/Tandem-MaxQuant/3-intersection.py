D = {}

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[7]
    D[pep] = line
inFile.close()

inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss')
ouFile1 = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation1', 'w')
ouFile2 = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation2', 'w')
ouFile3= open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation3', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    pep = fields[0]
    if pep in D:
        ouFile1.write(line + '\n')
        ouFile2.write(D[pep] + '\n')
    else:
        ouFile3.write(pep+'\n')
inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()


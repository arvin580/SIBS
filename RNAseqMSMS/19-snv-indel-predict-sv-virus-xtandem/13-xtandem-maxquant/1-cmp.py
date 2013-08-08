D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[6]
    D[pep] = 1
inFile.close()

n = 0
N = 0
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[7]
    N += 1
    if pep in D:
        n += 1
inFile.close()
print(n)
print(N)


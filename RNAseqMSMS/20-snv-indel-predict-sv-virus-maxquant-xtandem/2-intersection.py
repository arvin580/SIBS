L = []
L2 = []
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[7]
    L.append(pep)
inFile.close()


inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-pFind3-pFind-Trypsin')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[9]
    L2.append(pep)
inFile.close()

S = set(L)
S2 = set(L2)


S_minus_S2= S - S2
S2_minus_S = S2 -S
S_and_S2 = S & S2

print(len(S_minus_S2))
print(len(S2_minus_S))
print(len(S_and_S2))



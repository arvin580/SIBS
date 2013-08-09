D = {}
D2 = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_predict-pFind3')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[9]
    if fields[0] == 'pFind':
        D.setdefault(pep,[])
        D[pep].append(line) 
    D2.setdefault(pep,[])
    D2[pep].append(line) 
inFile.close()
print(len(D))
print(len(D2))


n = 0
N = 0
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-sequest-pFind','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    pep = fields[7]
    N += 1
    if pep in D:
        ouFile.write('pFind' + '\t' + line + '\n')
        n += 1
    else:
        ouFile.write('' + '\t' + line + '\n')
inFile.close()

print(n)
print(N)


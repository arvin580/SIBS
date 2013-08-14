D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest-type','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    tp = fields[11]
    D.setdefault(tp, 0)
    D[tp] += 1
inFile.close()

for k in D:
    ouFile.write(k+'\t'+str(D[k])+'\n')
ouFile.close()

def cleavage(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        D.setdefault(fields[6], 0)
        D[fields[6]] += 1
    inFile.close()
    for k in D:
        print(k+'\t'+str(D[k]))

cleavage('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')

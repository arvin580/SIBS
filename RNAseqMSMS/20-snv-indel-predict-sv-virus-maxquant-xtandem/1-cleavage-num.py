def cleavage(inF,i):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        D.setdefault(fields[i], 0)
        D[fields[i]] += 1
    inFile.close()
    for k in D:
        print(k+'\t'+str(D[k]))

#cleavage('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest',6)
#cleavage('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-pFind3-pFind',8)
cleavage('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_predict-pFind3-pFind',8)

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-spec')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict-spec.fasta','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ouFile.write('>' + '|'.join(fields)+'\n')
    ouFile.write(fields[0] + '\n')
inFile.close()
ouFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_predict-spec')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_predict-spec.fasta','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ouFile.write('>' + '|'.join(fields)+'\n')
    ouFile.write(fields[0] + '\n')
inFile.close()
ouFile.close()

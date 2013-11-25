D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[7]
    D.setdefault(pep, [])
inFile.close()

ouFile = open('Identified-Peptides-Corresponding-Reads', 'w')
inFile = open('HeLa_known-predicted-snv-indel-sv-virus-KR.fasta')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        for k in D:
            if k in line2:
                D[k].append(line1)
    else:
        break
inFile.close()
for k in D:
    ouFile.write(k + '\t' + '\t'.join(D[k])+'\n')
ouFile.close()

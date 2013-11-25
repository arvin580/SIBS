D = {}
inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-sequest')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[7]
    num = int(fields[8].split(';')[0])
    D.setdefault(pep, num)
inFile.close()

ouFile = open('Identified-Peptides-Corresponding-Spectrums', 'w')
d = D.items()
d.sort(cmp = lambda x,y :cmp(x[1], y[1]), reverse = True)
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1]) + '\n')

ouFile.close()

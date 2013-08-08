inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L = []
    for i in range(len(fields)):
        if fields[i].find('Velos1_NaNa')!=-1:
            f = fields[i].strip()
            #no = fields[i+27]
            #fno = f + ':' + no
            L.append(f)
    ouFile.write('\t'.join(fields[0:8])+'\t'+';'.join(L)+'\t'+'\t'.join(fields[8:])+'\n')
inFile.close()
ouFile.close()

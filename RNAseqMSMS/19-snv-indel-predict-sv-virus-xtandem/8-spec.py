inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-spec','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L = []
    for i in range(len(fields)):
        if fields[i].find('Velos1_NaNa')!=-1:
            f = fields[i]
            #no = fields[i+27]
            #fno = f + ':' + no
            L.append(f)
    ouFile.write('\t'.join(fields[0:7])+'\t'+';'.join(L)+'\t'+'\t'.join(fields[7:])+'\n')
inFile.close()
ouFile.close()

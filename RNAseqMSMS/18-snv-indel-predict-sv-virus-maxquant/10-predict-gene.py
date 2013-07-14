inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_predict-gene_pep_num','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[3]
    if gene:
        D.setdefault(gene, 0)
        D[gene] += 1
d = D.items()
d.sort(cmp=lambda x,y :cmp(x[1],y[1]),reverse=True)
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')
inFile.close()
ouFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_minus-spec-to_validation_not_predict-gene_pep_num','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    genes = fields[3].split(':')
    for gene in genes:
        if gene!='*':
            D.setdefault(gene, 0)
            D[gene] += 1
d = D.items()
d.sort(cmp=lambda x,y :cmp(x[1],y[1]),reverse=True)
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')
inFile.close()
ouFile.close()


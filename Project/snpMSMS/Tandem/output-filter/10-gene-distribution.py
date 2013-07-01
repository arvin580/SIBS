inFile = open('Liver-SNV-INDEL-new-pep-gene-new-pFind3-new_pFind')
ouFile = open('Liver-SNV-INDEL-new-pep-gene-new-pFind3-new_pFind-gene-distribution','w')
D = {}
D2 = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[5]
    D.setdefault(gene,{})
    for item in fields[6:]:
        sample = item.split('.')[0]
        D[gene].setdefault(sample,0)
        D[gene][sample] += 1
        D2[sample] = 0
inFile.close()

ouFile.write('gene\t')
for s in D2: 
    ouFile.write(s+'\t')
ouFile.write('\n')

for k in D:
    for s in D2:
        if s in D[k]:
            ouFile.write(str(D[k][s])+'\t')
        else:
            ouFile.write(str(D2[s])+'\t')
    ouFile.write('\n')

ouFile.close()

ouFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two','w')
D = {}
def combine(inF, tp):
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        gene = fields[0]
        x = fields[0].split(':')
        for y in x:
            if y != '*':
                z = y.split('|')
                for m in z:
                    if m:
                        D.setdefault(m, [])
                        D[m].append(tp+'\t'+line)
    inFile.close()

combine('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_two','Deletion')
combine('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_two','Duplication')
combine('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_two','Inversion')
combine('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_two','Translocation')

for k in D:
    for j in D[k]:
        ouFile.write(k+ '\t' + j)
ouFile.close()

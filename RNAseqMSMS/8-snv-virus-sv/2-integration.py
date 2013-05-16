### [SNV, Virus, SV]
D = {}
inFile = open('sum_snv.exome_summary.overall.filter')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[1]
    D.setdefault(gene,[0,0,0])
    D[gene][0] = 1
inFile.close()


inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene3')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0])
    D[gene][1] = 1
inFile.close()

inFile = open('split-mapped-deletion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0])
    D[gene][2] = 1
inFile.close()

inFile = open('split-mapped-duplication.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0])
    D[gene][2] = 1
inFile.close()

inFile = open('split-mapped-inversion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0])
    D[gene][2] = 1
inFile.close()

inFile = open('split-mapped-translocation.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0])
    D[gene][2] = 1
inFile.close()

d = D.items()
d.sort(cmp= lambda x,y:cmp(sum(x[1]),sum(y[1])),reverse= True)

ouFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation2','w')
for item in d:
    ouFile.write(item[0]+'\t'+'\t'.join([str(x) for x in item[1]])+'\n')

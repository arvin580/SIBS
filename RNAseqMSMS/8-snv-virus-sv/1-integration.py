### [SNV, Virus, Deltion, Duplication, Inversion, Translocation]
inFile = open('sum_snv.exome_summary.overall.filter')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[1]
    D.setdefault(gene,[0,0,0,0,0,0])
    D[gene][0] = 1
inFile.close()


inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene3')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene,[0,0,0,0,0,0])
    D[gene][1] = 1
inFile.close()

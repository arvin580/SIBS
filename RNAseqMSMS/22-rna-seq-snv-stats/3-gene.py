def gene(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        fields = line.split('\t')
        gene = fields[1]
        x = gene.split('(')[0]
        y = x.split(';')
        for z in y:
            m = z.split(',')
            for n in m:
                D[n] = 1
    for x in D:
        ouFile.write(x+'\n')

    inFile.close()
    ouFile.close()

gene('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing')
gene('sum_snv.exome_summary.indel.overall.filter')
gene('sum_snv.exome_summary.indel.overall.filter-dbsnp')

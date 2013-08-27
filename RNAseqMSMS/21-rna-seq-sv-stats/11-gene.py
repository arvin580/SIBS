def gene(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        g = fields[0]
        if g:
            gs = g.split('|')
            for x in gs:
                D.setdefault(x, 0)
                D[x] += 1

    inFile.close()
    d = D.items()
    d.sort(cmp= lambda x,y:cmp(x[1],y[1]),reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' +str(item[1])+ '\n')
    ouFile.close()

def gene2(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        g = fields[0]
        if g:
            gs = g.split(':')
            for x in gs:
                if x!= '*':
                    y = x.split('|')
                    for z in y:
                        D.setdefault(z, 0)
                        D[z] += 1

    inFile.close()
    d = D.items()
    d.sort(cmp= lambda x,y:cmp(x[1],y[1]),reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' +str(item[1])+ '\n')
    ouFile.close()


gene('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_two')
gene('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_two')
gene('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_two')
gene2('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_two')

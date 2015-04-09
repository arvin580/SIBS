inFile = open('delly.1.sv.stat.gene.symbol.heatmap')
ouFile = open('delly.1.sv.stat.gene.symbol.heatmap.sym','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0].split(':')
    for x in gene:
        if x !='*':
            y = x.split('/')
            for z in y:
                D[z]=fields[1:]
inFile.close()
for k in D:
    ouFile.write(k+'\t'+'\t'.join(D[k])+'\n')

ouFile.close()

inFile = open('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap')
ouFile = open('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap.sym','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0].split(':')
    for x in gene:
        if x !='*':
            y = x.split('/')
            for z in y:
                D[z]=fields[1:]
inFile.close()
for k in D:
    ouFile.write(k+'\t'+'\t'.join(D[k])+'\n')

ouFile.close()

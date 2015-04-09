def symbol(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.sym','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[0:1]:
            fds = item.split(':')
            for fd in fds:
                if fd != '*':
                    fs = fd.split('/')
                    for x in fs:
                        D[x]=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
    ouFile.close()

symbol('invy.jumpy.duppy.1.sv.stat.exon.symbol.heatmap')
symbol('invy.jumpy.duppy.1.sv.stat.exon.symbol.heatmap2')
symbol('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap')
symbol('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap2')
symbol('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap3')
symbol('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap4')
symbol('delly.1.sv.stat.exon.symbol.heatmap')
symbol('delly.1.sv.stat.exon.symbol.heatmap2')

D2 = {}
def symbol(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.sym','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[1:]:
            fds = item.split(':')
            for fd in fds:
                if fd != '*':
                    fs = fd.split('/')
                    for x in fs[0:1]:
                        D[x]=1
                        D2[x]=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
    ouFile.close()

symbol('delly.1.sv.stat.gene.symbol')
symbol('invy.1.sv.stat.gene.symbol')
symbol('duppy.1.sv.stat.gene.symbol')
symbol('jumpy.1.sv.stat.gene.symbol')

ouFile = open('delly.invy.duppy.jumpy.1.sv.stat.gene.symbol.sym','w')
for k in D2:
    ouFile.write(k+'\n')
ouFile.close()

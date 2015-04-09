import re


def symbol(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[1:]:
            fs = re.split('[/:]', item)
            for f in fs:
                if f != '*':
                    D.setdefault(f, 0)
                    D[f] += 1
    inFile.close()

D = dict()
symbol('delly.1.sv.stat.exon.symbol')
symbol('jumpy.1.sv.stat.exon.symbol')
symbol('invy.1.sv.stat.exon.symbol')
symbol('duppy.1.sv.stat.exon.symbol')

ouFile = open('1.sv.stat.exon.symbol', 'w')
for k in D:
    ouFile.write(k + '\n')

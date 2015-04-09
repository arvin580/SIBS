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
symbol('delition.exon.symbol')
symbol('translocation.exon.symbol')
symbol('inversion.exon.symbol')
symbol('duplication.exon.symbol')

ouFile = open('1.sv.stat.exon.symbol', 'w')
for k in D:
    ouFile.write(k + '\n')

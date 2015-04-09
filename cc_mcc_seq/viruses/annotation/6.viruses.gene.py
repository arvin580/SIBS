### py  6.viruses.gene.py *.gene
import sys

D = {}
ouFile = open('viruse.hg.gene.distribution','w')
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields) > 2:
            k = '/'.join(fields[2:])
            sample = inF.split('.')[0]
            D.setdefault(k, {})
            D[k].setdefault(sample, 0)
            D[k][sample]+=1
    inFile.close()

S = ['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B',
        'CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B']
for k in D:
    Data = [0]*len(S)
    for s in D[k]:
        Data[S.index(s)]=D[k][s]
    ouFile.write(k+'\t')
    ouFile.write('\t'.join([str(x) for x in Data])+'\n')

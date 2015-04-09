### py  3.hg.pos.py *.format
import sys

D = {}
ouFile = open('viruse.hg.pos.distribution','w')
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0].find('chr')==0:
            pos = int(fields[1])
            k = fields[0].split('.')[0]+':'+str(pos)
            sample = inF.split('.')[0]
            D.setdefault(k, {})
            D[k].setdefault(sample, 0)
            D[k][sample]+=1
    inFile.close()

def cmp_fun(x,y):
    if x[0].split(':')[0] < y[0].split(':')[0]:
        return -1
    elif x[0].split(':')[0] > y[0].split(':')[0]:
        return 1
    else :
        if int(x[0].split(':')[1]) < int(y[0].split(':')[1]):
            return -1
        elif int(x[0].split(':')[1]) > int(y[0].split(':')[1]):
            return 1
        else:
            return 0

S = ['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B',
        'CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B']
d = D.items()
d.sort(cmp = lambda x,y :cmp_fun(x,y))
for k in d:
    Data = [0]*len(S)
    for s in k[1]:
        Data[S.index(s)]=k[1][s]
    ouFile.write(k[0]+'\t')
    ouFile.write('\t'.join([str(x) for x in Data])+'\n')

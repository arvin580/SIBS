#!/usr/bin/env python
import sys
inFile = open(sys.argv[1])
D = {}
chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
        'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16',
        'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22',
        'chrX', 'chrY', 'chrM']
while True:
    seq1 = inFile.readline().strip()
    seq2 = inFile.readline().strip()
    if seq1:
        fields1 = seq1.split('\t')
        fields2 = seq2.split('\t')
        k1 = fields1[2]+'\t'+fields2[2]
        k2 = fields2[2]+'\t'+fields1[2]
        if k1 not in D and k2 not in D:
            if chrs.index(fields1[2]) <= chrs.index(fields2[2]):
                D.setdefault(k1, [])
                D[k1].append([int(fields1[3]), int(fields2[3])])
            elif chrs.index(fields1[2]) > chrs.index(fields2[2]):
                D.setdefault(k2, [])
                D[k2].append([int(fields2[3]), int(fields1[3])])
        elif k1 in D:
            D[k1].append([int(fields1[3]), int(fields2[3])])
        elif k2 in D:
            D[k2].append([int(fields2[3]), int(fields1[3])])
    else:
        break
ouFile = open(sys.argv[1]+'.sorted', 'w')

def cmp_fun(x , y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0
def cmp_fun2(x, y):
    if chrs.index(x[0].split('\t')[0]) < chrs.index(y[0].split('\t')[0]):
        return -1
    elif chrs.index(x[0].split('\t')[0]) > chrs.index(y[0].split('\t')[0]):
        return 1
    else:
        if chrs.index(x[0].split('\t')[1]) < chrs.index(y[0].split('\t')[1]):
            return -1
        elif chrs.index(x[0].split('\t')[1]) > chrs.index(y[0].split('\t')[1]):
            return 1
        else:
            return 0

d = D.items()
d.sort(cmp = lambda x,y :cmp_fun2(x,y))
for item in d:
    item[1].sort(cmp=lambda x,y:cmp_fun(x,y))
    for it in item[1]:
        ouFile.write(item[0] + '\t' + str(it[0]) + '\t' +str(it[1]) + '\n')

inFile.close()
ouFile.close()

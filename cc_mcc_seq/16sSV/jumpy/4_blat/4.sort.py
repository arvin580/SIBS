import sys
inFile = open(sys.argv[1])
D = {}
while True:
    seq1 = inFile.readline().strip()
    seq2 = inFile.readline().strip()
    if seq1:
        fields1 = seq1.split('\t')
        fields2 = seq2.split('\t')
        k1 = fields1[2]+'\t'+fields2[2]
        k2 = fields2[2]+'\t'+fields1[2]
        if k1 not in D and k2 not in D:
            D.setdefault(k1, [])
            D[k1].append([int(fields1[3]), int(fields2[3])])
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
for k in D:
    D[k].sort(cmp=lambda x,y:cmp_fun(x,y))
    for item in D[k]:
        ouFile.write(k + '\t' + str(item[0]) + '\t' +str(item[1]) + '\n')


inFile.close()
ouFile.close()

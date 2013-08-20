ouFile = open('HeLa-deletion-duplication-inversion-translocaton-num','w')

def num(inF,flag):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D.setdefault(int(fields[1]), 0)
        D[int(fields[1])] += 1
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y:cmp(x[0],y[0]))
    ouFile.write(flag+'\t')
    for item in d :
        ouFile.write(str(item[0]) + '\t' + str(item[1])+'\t')
    ouFile.write('\n')

num('split-mapped-inversion.normal.seq.filtered.num.mc','Inversion')
num('split-mapped-duplication.normal.seq.filtered.num.mc','Duplication')
num('split-mapped-deletion.normal.seq.filtered.num.mc','Deletion')
num('split-mapped-translocation.normal.seq.filtered.num.mc','Translocation')

ouFile.close()

def num(inF):
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
    for item in d :
        print(str(item[0]) + '\t' + str(item[1]))

num('split-mapped-inversion.normal.seq.filtered.num')
num('split-mapped-duplication.normal.seq.filtered.num')

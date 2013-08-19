def num(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')

        ch = fields[3]
        query_start1 = int(fields[8])
        query_end1 = int(fields[9])
        query_start2 = int(fields[20])
        query_end2 = int(fields[21])

        subject_start1 = int(fields[10])
        subject_end1 = int(fields[11])
        subject_start2 = int(fields[22])
        subject_end2 = int(fields[23])

        if (query_start1 + query_end1) <= (query_start2 + query_end2):
            point = subject_end1
        else:
            point = subject_end2
        k = ch + ':' + str(point)
        D.setdefault(k, [])
        D[k].append(line)
    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])),reverse = True)
    for item in d:
        print(item[0])
        print('\n'.join(item[1]))

num('split-mapped-inversion.normal.seq')

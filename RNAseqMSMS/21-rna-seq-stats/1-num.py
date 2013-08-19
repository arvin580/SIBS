def num(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '.seq','w')
    while True:
        line1 = inFile.readline().rstrip()
        line2 = inFile.readline().rstrip()
        if line1:
            fields = line1.split('\t')
            k = '\t'.join(fields[0:-1])
            D.setdefault(k, [])
            D[k].append(line2)
        else:
            break
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
    ouFile.close()

num('split-mapped-inversion.normal')
num('split-mapped-duplication.normal')
num('split-mapped-deletion.normal')
num('split-mapped-translocation.normal')



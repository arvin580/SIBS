def num(inF):
    inFile = open(inF)
    ouFile = open(inF+'.read-name', 'w')
    D = {}
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split()
            D.setdefault(fields[0], 0)
            D[fields[0]]+=1
        else:
            break
    inFile.close()
    for k in D:
        ouFile.write(k + str(D[k]) + '\n')
    ouFile.close()


num('split-mapped-translocation')
num('split-mapped-inversion')
num('split-mapped-duplication')
num('split-mapped-deletion')


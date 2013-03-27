def cleavge(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        if len(fields)>3:
            if fields[2]:
                D.setdefault(fields[2][-1],0)
                D[fields[2][-1]]+=1
    inFile.close()
    print(inF)
    print(D)

cleavge('msb201181-s2-peptides-gluc.txt')
cleavge('msb201181-s2-peptides-lysc.txt')
cleavge('msb201181-s2-peptides-trypsin.txt')
        

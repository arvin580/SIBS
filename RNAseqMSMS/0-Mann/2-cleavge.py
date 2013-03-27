def cleavge(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        if len(fields)>3:
            D[fields[2][-1]]=1
    inFile.close()
    print(D)

cleavge('msb201181-s2-peptides-gluc.txt')
        

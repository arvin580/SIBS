def num(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '.num', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('+++')
            D[line2] = len(fields) 
        else:
            break
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y:cmp(x[1],y[1]), reverse=True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(item[1]) + '\n')
    ouFile.close()

num('Peptides-Identified-Second-unSpec')

def delly(inF):
    inFile = open(inF)
    D = {}
    for line in inFile:
        line = line.strip()
        if line.find('>')==0:
            fields = line.split(':')
            D.setdefault(fields[2], [])
            D[fields[2]].append(fields[3:7])
    inFile.close()
    n = 0
    for k in D:
        ouFile = open(k+'.translocation', 'w')
        for item in D[k]:
            n+=1
            ouFile.write('tran'+str(n)+'\t'+item[0]+'\t'+item[1]+'\t'+item[1]+'\n')
            ouFile.write('tran'+str(n)+'\t'+item[2]+'\t'+item[3]+'\t'+item[3]+'\n')
        ouFile.close()
delly('translocation.gene.reads')



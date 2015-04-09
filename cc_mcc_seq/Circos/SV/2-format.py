def duppy(inF):
    inFile = open(inF)
    D = {}
    for line in inFile:
        line = line.strip()
        if line.find('>')==0:
            fields = line.split(':')
            D.setdefault(fields[1], [])
            D[fields[1]].append(fields[2:5])
    inFile.close()
    n = 0
    for k in D:
        ouFile = open(k+'.duplication', 'w')
        for item in D[k]:
            n+=1
            ouFile.write('dup'+str(n)+'\t'+item[0]+'\t'+item[1]+'\t'+item[1]+'\n')
            ouFile.write('dup'+str(n)+'\t'+item[0]+'\t'+item[2]+'\t'+item[2]+'\n')
        ouFile.close()
duppy('duplication.gene.reads')



def gene(inF):
    D = {}
    D2 = {}
    inFile = open(inF)
    ouFile1 = open(inF+'.gene1','w')
    ouFile2 = open(inF+'.gene2','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[3]
        pep = fields[2]
        fds = gene.split(':')
        for fd in fds:
            fs = fd.split('|')
            for y in fs:
                ys = y.split(';')
                for x in ys:
                    if x !='*' and x!='': 
                        D.setdefault(x,[])
                        D2.setdefault(x,[])
                        D[x].append(pep)
                        D2[x].append(line)
    inFile.close()
    for k in D:
        D[k]=set(D[k])

    d = D.items()
    d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)
    for item in d:
        ouFile1.write(item[0]+'\t'+'\t'.join(item[1])+'\n')
        ouFile2.write(item[0]+'\t'+'\t'.join(D2[item[0]])+'\n')
    ouFile1.close()
    ouFile2.close()

gene('HeLa-SNV-INDEL-VIRUS-SV-pep')

def gene2(inF):
    D = {}
    D2 = {}
    inFile = open(inF)
    ouFile1 = open(inF+'.gene1','w')
    ouFile2 = open(inF+'.gene2','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        pep = fields[6]
        fds = gene.split(':')
        for fd in fds:
            fs = fd.split('|')
            for y in fs:
                ys = y.split(';')
                for x in ys:
                    if x !='*' and x!='': 
                        D.setdefault(x,[])
                        D2.setdefault(x,[])
                        D[x].append(pep)
                        D2[x].append(line)
    inFile.close()
    for k in D:
        D[k]=set(D[k])

    d = D.items()
    d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)
    for item in d:
        ouFile1.write(item[0]+'\t'+'\t'.join(item[1])+'\n')
        ouFile2.write(item[0]+'\t'+'\t'.join(D2[item[0]])+'\n')
    ouFile1.close()
    ouFile2.close()

gene2('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind')
gene2('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind_ALL_UNIQUE')
gene2('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind_ONE_UNIQUE')

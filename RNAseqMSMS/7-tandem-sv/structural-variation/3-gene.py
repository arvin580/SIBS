def gene(inF):
    D1 = {}
    D2 = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        fds = gene.split(':')
        for fd in fds:
            it = fd.split('|')
            for x in it:
                if x != '*' and x != '':
                    D1.setdefault(x,[])
                    D2.setdefault(x,[])
                    D1[x].append(line)
                    D2[x].append(fields[0])

    inFile.close()
    for k in D1:
        ouFile.write(k+'\t'+'\t'.join(set(D2[k]))+'\t'+'\t'.join(D1[k])+'\n')

    ouFile.close()

gene('HeLa-SV-Deletion-pep.full-cleavage.gene')
gene('HeLa-SV-Duplication-pep.full-cleavage.gene')
gene('HeLa-SV-Inversion-pep.full-cleavage.gene')
gene('HeLa-SV-Translocation-pep.full-cleavage.gene')


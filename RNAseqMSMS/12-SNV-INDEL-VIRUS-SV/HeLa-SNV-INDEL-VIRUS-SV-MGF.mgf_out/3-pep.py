def pep(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[1]:
            D.setdefault(fields[1],[])
            D[fields[1]].append(0)
        if fields[2]:
            D.setdefault(fields[2],[])
            D[fields[2]].append(2)
        if fields[3]:
            D.setdefault(fields[3],[])
            D[fields[3]].append(3)
        fds = fields[4].split(':')
        i = 4
        for item in fds:
            D.setdefault(item,[])
            D[item].append(i)
            i += 1
    inFile.close()
    ouFile = open(inF+'.pep3','w')
    for k in D:
        if 0 in D[k]:
            ouFile.write(k+'\n')
    ouFile.close()


pep('0.ED-2013_05_31_16_23_30_qry.peptides-pep')
pep('0.K-2013_06_01_09_57_53_qry.peptides-pep')
pep('0.ED-2013_06_01_09_57_53-K8R10_qry.peptides-pep')
pep('0.KR-2013_05_31_15_31_15_qry.peptides-pep')
pep('0.ED-2013_06_01_09_57_53_qry.peptides-pep')
pep('0.KR-2013_06_01_09_57_53-K8R10_qry.peptides-pep')
pep('0.K-2013_05_31_15_31_15_qry.peptides-pep')
pep('0.KR-2013_06_01_09_57_53_qry.peptides-pep')
pep('0.K-2013_06_01_09_57_53-K8R10_qry.peptides-pep')


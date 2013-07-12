def unique(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0]+'-unique','w')
    inFile.readline()
    D = {}
    for line in inFile:
        line = line.strip()
        fields = line.split()
        pep = fields[0]
        D.setdefault(pep,[])
        D[pep].append(line)
    inFile.close()
    
    for k in D:
        ouFile.write(k+'\t'+str(len(D[k]))+'\t'+'\t'.join(D[k])+'\n')
    ouFile.close()

unique('HeLa-variant-Trypsin-evidence.txt')
unique('HeLa-variant-LysC-evidence.txt')
unique('HeLa-variant-GluC-evidence.txt')

unique('HeLa-known-Trypsin-evidence.txt')
unique('HeLa-known-LysC-evidence.txt')
unique('HeLa-known-GluC-evidence.txt')

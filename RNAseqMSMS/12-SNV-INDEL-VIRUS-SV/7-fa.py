import os

D = {}
Files = os.listdir('.')
for F in Files:
    if F == 'HeLa-SNV-INDEL-VIRUS-SV-MGF.note':
        inFile = open(F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            D.setdefault(fields[0],[])
            D[fields[0]].append(fields[1]+':'+fields[2])
        inFile.close()

ouFile = open('HeLa-SNV-INDEL-VIRUS-SV-MGF.fa','w')
for k in D:
    ouFile.write('>'+k+'|'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
ouFile.close()

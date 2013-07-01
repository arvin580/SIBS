import os

D = {}
Files = os.listdir('.')
for F in Files:
    if F[-5:] == '.note':
        inFile = open(F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            D.setdefault(fields[0],[F.split('-pep-spec.note')[0]])
            D[fields[0]].append(fields[1])
        inFile.close()

ouFile = open('HeLa-SNV-Virus-SV.fa','w')
for k in D:
    ouFile.write('>'+k+'|'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
ouFile.close()

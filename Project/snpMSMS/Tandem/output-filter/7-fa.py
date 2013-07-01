import os

D = {}
Files = os.listdir('.')
for F in Files:
    if F == 'Liver-SNV-INDEL-new-pep-spec.note':
        inFile = open(F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            D.setdefault(fields[0],[])
            D[fields[0]].append(fields[1]+':'+fields[2])
        inFile.close()

ouFile = open('Liver-SNV-INDEL-pep-MGF.fa','w')
for k in D:
    ouFile.write('>'+k+'|'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
ouFile.close()

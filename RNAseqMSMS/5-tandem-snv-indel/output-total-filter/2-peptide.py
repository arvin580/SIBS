inFile = open('HeLa-SNV-INDEL-ALT')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[3], [])
    D[fields[3]].append(fields[1])

inFile.close()

ouFile = open('HeLa-SNV-INDEL-ALT-pep','w')
for k in D:
    v = '\t'.join(D[k])
    if v.find('SNV')!=-1:
        ouFile.write(k+'\t'+v+'\n')
for k in D:
    v = '\t'.join(D[k])
    if v.find('INDEL')!=-1:
        ouFile.write(k+'\t'+v+'\n')

ouFile.close()

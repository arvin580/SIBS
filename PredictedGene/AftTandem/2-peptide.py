inFile = open('HeLa-peptide-Predicted')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[4]
    D.setdefault(pep, []) 
    D[pep].append(line)
inFile.close()

ouFile = open('HeLa-peptide-Predicted-pep','w')
for k in D:
    fields = D[k][0].split('\t')
    ouFile.write(k+'\t'+str(len(D[k]))+'\t'+'\t'.join(D[k])+'\n')
ouFile.close()

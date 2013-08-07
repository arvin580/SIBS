inFile = open('HeLa-peptide-snv-indel-predict-sv-virus')

D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[5]
    D.setdefault(pep, []) 
    D[pep].append(line)
inFile.close()

ouFile = open('HeLa-peptide-snv-indel-predict-sv-virus-trypsin-pep','w')
for k in D:
    fields = D[k][0].split('\t')
    ouFile.write(fields[0]+'\t'+fields[1]+'\t'+k+'\t'+str(len(D[k]))+'\t'+'\t'.join(D[k])+'\n')
ouFile.close()

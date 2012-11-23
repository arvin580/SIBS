D = {}
CL = ['97H','97L','Hep3B','LM3','LM6','SNU398','SNU449','SNU475']
inFile = open('tandem.peptides.stopgain.candidates.gene2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], {})
    D[fields[0]].setdefault(fields[1],[0]*8)
    for c in range(2,len(fields),2):
        D[fields[0]][fields[1]][CL.index(fields[c])]=int(fields[c+1])
inFile.close()

inFile = open('tandem.peptides.uniprot.candidates.gene2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], {})
    D[fields[0]].setdefault(fields[1],[0]*8)
    for c in range(2,len(fields),2):
        D[fields[0]][fields[1]][CL.index(fields[c])]=int(fields[c+1])
inFile.close()

d = D.items()


ouFile = open('tandem.peptides.stopgain.uniprot.gene.distribution', 'w')
for k in D:
    for k2 in D[k]:
        ouFile.write(k+'\t'+k2+'\t'+'\t'.join([str(x) for x in D[k][k2]])+'\n')

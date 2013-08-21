D = {}
inFile = open('/netshare1/home1/people/hansun/Data/Aging/genage_human.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[2],0)
    D[fields[2]]+=1
    for item in fields[1].split():
        D.setdefault(item,0)
        D[item]+=1
inFile.close()
print(len(D))

def gene(inF):
    inFile = open(inF)
    ouFile = open(inF+'.aging','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        if gene in D:
            ouFile.write(gene+'\n')
    inFile.close()

gene('split-mapped-deletion-inversion-duplication-translocation.gene.4-type')
gene('split-mapped-deletion-inversion-duplication-translocation.gene.3-type')
gene('split-mapped-deletion-inversion-duplication-translocation.gene.2-type')
gene('split-mapped-deletion-inversion-duplication-translocation.gene.1-type')

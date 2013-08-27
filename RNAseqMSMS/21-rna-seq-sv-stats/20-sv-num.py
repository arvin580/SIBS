inFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two')
ouFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num','w')
D = {}
for line in inFile:
    fields = line.split('\t')
    gene = fields[0]
    D.setdefault(gene, 0)
    D[gene] += 1
inFile.close()

d = D.items()
d.sort(cmp= lambda x,y:cmp(x[1],y[1]),reverse=True)
for item in d:
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')
ouFile.close()

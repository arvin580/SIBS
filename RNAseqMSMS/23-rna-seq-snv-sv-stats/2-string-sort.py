D = {}


inFile = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

S = {}
SL = {}
inFile = open('protein.links.v9.05.human.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    S.setdefault(gene, [])
    SL[gene] = len(fields)
    for item in fields:
        if item in D:
            S[gene].append(item)
inFile.close()
ouFile1 = open('HeLa-mutated-gene-num2','w')
ouFile2 = open('HeLa-mutated-genes2','w')
for k in S:
    ouFile1.write(k + '\t' +str(SL[k]) +'\t'+str(len(S[k]))+'\n')
    ouFile2.write(k + '\t' + '\t'.join(S[k])+'\n') 

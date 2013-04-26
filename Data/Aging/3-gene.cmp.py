D = {}
inFile = open('genage_human.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[2],0)
    D[fields[2]]+=1
    for item in fields[1].split():
        D.setdefault(item,0)
        D[item]+=1
inFile.close()

def gene(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        if gene in D:
            print(gene)
    inFile.close()

gene('HeLa-SNV-INDEL-ALT-pep.gene')

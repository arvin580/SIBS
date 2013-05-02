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

gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene')
gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-2236-2244-human-gene')
gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-1420-1428-human-gene')
gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-439-447-human-gene')

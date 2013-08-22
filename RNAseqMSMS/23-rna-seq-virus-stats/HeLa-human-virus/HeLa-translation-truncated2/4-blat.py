D = {}
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.fa.blated')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0].split(':')[0]
    v = int(fields[0].split(':')[-1])
    D.setdefault(k,['']*6)
    pos = fields[1]+':'+fields[6]+':'+fields[7]+':'
    D[k][v]+=pos
inFile.close()
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.fa.blated2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0].split(':')[0]
    v = int(fields[0].split(':')[-1])
    D.setdefault(k,['']*6)
    pos = fields[1]+':'+fields[6]+':'+fields[7]+':'
    D[k][v]+=pos
inFile.close()


for k in D:
    print(k)
    print(D[k])

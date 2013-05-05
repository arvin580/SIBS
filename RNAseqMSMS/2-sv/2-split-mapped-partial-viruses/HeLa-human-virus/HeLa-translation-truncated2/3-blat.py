D = {}
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.fa.blated')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0].split(':')[0]
    v = int(fields[0].split(':')[-1])
    D.setdefault(,[-6]*6)
    D[v]=fields[1]+':'+fields[6]+':'+fields[7]
inFile.close()

for k in D:
    print(k)
    print(D[k])

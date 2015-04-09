import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.split','w')
D = dict()
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], [])
    D[fields[0]].append(line)
inFile.close()

for k in D:
    c = 0
    v = 0
    for item in D[k]:
        if item.find('chr')!=-1:
            c += 1
        if item.find('NC')!=-1:
            v += 1
    if c and v:
        for item in D[k]:
            ouFile.write(item + '\n')

inFile.close()
ouFile.close()
        


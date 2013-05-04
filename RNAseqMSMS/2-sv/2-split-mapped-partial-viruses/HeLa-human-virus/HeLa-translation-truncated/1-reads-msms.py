D = {}
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip('>\n')
    if line1:
        fields = line1.split('\t')
        D[fields[0]]=1
    else:
        break
inFile.close()

D2 = {}
inFile = open('HeLa-Known-Protein')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields:
        its = item.split(':')
        for it in its:
            if it in D:
                D2.setdefault(it,[])
                D2[it].append(line)
inFile.close()

for k in D2:
    print(k)
    print(D2[k])


inFile = open('3-stopgain-protein')
ouFile = open('3-stopgain-protein-unique','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D = {}
    for x in fields[1:]:
        D[x]=1
    ouFile.write(fields[0]+'\t')
    for k in D:
        ouFile.write(k+'\t')
    ouFile.write('\n')
inFile.close()
ouFile.close()

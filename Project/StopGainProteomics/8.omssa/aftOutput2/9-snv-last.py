inFile = open('3-stopgain-protein-unique2-filtered.blated.filtered.snv')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0].split(':')[1]
    D[pep]=1
inFile.close()


inFile = open('3-stopgain-protein-unique-filtered2')
ouFile = open('3-stopgain-protein-unique-filtered2.snv','w')
for line in inFile:
    for k in D:
        if line.find(k)!=-1:
            ouFile.write(line)
            break
inFile.close()
ouFile.close()

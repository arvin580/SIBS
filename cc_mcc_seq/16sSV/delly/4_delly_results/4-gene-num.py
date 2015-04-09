inFile = open('1.sv.stat.gene')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[1:]:
        fds = item.split(':')
        if len(fds) ==4:
            D[':'.join(fds[0:-1])]=1
inFile.close()
print(len(D))

inFile = open('1.sv.stat.gene.dbsnp2')
D2={}
for line in inFile:
    line = line.strip()
    if line.find('chr')==0:
        k = ':'.join(line.split('\t'))
        if k in D:
            D2[k]=1
inFile.close()
print(len(D2))



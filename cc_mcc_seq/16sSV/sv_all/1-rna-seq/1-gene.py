inFile = open('potential_fusion.txt')
ouFile = open('potential_fusion.gene','w')
D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()
    if line1:
        fields = line5.split()
        fds = line1.split()
        D.setdefault(fields[0], [])
        D[fields[0]].append(fds[0]+':'+fields[1])
        D[fields[0]].append(fds[0]+':'+fields[3])

    else:
        break
inFile.close()

D2 = {}
def sv(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        if line.find('>') == 0:
            line = line.strip('>')
            fields = line.split(':')
            gene =fields[0]
            D2.setdefault(gene, [])
            D2[gene].append(line)
    inFile.close()

sv('delition.gene.reads')
sv('duplication.gene.reads')
sv('inversion.gene.reads')
sv('translocation.gene.reads')


for k in D2:
    if k in D:
        ouFile.write(k+'\n')
ouFile.close()

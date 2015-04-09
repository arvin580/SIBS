import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.top','w')
ouFile2 = open(sys.argv[1]+'.top2','w')
if sys.argv[1].find('ICC4A')==0:
     for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if float(fields[2])>95 and float(fields[3])>65:
            D.setdefault(fields[0], [])
            D[fields[0]].append(line)
else:
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if float(fields[2])>95 and float(fields[3])>90:
            D.setdefault(fields[0], [])
            D[fields[0]].append(line)
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1][0].split('\t')[1],y[1][0].split('\t')[1]))

for item in d:
    ouFile.write(item[1][0]+'\n')
    if len(item[1]) > 1:
        for x in item[1]:
            ouFile2.write(x+'\n')



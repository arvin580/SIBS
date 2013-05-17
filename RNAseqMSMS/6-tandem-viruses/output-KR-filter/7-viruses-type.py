import sys
D = {}
inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'.type-viruse', 'w')
while True:
    line1 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        if fields[1].find('NC')==0:
            D.setdefault(fields[1], 0)
            D[fields[1]]+=1
    else:
        break

inFile.close()
print(D)

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]),reverse=True)

for item in d:
    if item[0].find('NC')==0:
        ouFile1.write(item[0] + '\t' + str(item[1]) + '\n')

ouFile1.close()

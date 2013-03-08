import sys
D = {}
inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'.type-viruse', 'w')
ouFile2 = open(sys.argv[1]+'.type-chr', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split()
        if (fields[3].find('chr')==0 and fields[15].find('NC') == 0) or \
            (fields[15].find('chr')==0 and fields[3].find('NC') == 0):
            D.setdefault(fields[3], 0)
            D.setdefault(fields[15], 0)
            D[fields[3]]+=1
            D[fields[15]]+=1
    else:
        break

inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]))

for item in d:
    if item[0].find('chr')==0:
        ouFile2.write(item[0] + '\t' + str(item[1]) + '\n')
    if item[0].find('NC')==0:
        ouFile1.write(item[0] + '\t' + str(item[1]) + '\n')

ouFile1.close()
ouFile2.close()

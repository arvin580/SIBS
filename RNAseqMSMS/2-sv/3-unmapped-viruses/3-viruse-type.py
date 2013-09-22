### python  3-viruse-type.py unmapped-blated-viruses-90-60.seq
import sys
D = {}
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.type', 'w')
while True:
    line = inFile.readline()
    line2 = inFile.readline()
    if line:
        line = line.strip()
        fields = line.split()
        if len(fields) == 12:
            D.setdefault(fields[1], 0)
            D[fields[1]] += 1
    else:
        break
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]))

for item in d:
    ouFile.write(item[0] + '\t' + str(item[1]) + '\n')

ouFile.close()

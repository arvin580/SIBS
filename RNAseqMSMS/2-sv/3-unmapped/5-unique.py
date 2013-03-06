import sys
D = {}

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.unique','w')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        D.setdefault(line2,[])
        D[line2].append(line1)
    else:
        break

for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')

inFile.close()
ouFile.close()

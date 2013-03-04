import sys
inFile = open(sys.argv[1])
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]]=1
inFile.close()

inFile = open(sys.argv[1].split('.blated')[0])
ouFile = open(sys.argv[1]+'.unmapped', 'w')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        if line1 not in D:
            ouFile.write('>'+line1+'\n')
            ouFile.write(line2+'\n')
    else:
        break
inFile.close()
ouFile.close()

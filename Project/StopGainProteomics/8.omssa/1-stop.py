import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.stop','w')
for line in inFile:
    fields = line.split(',')
    pep = fields[2]
    if pep[-1]=='K' or pep[-1]=='R':
        pass
    else:
        ouFile.write(fields[2]+'w')
inFile.close()

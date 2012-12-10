import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.recurrent', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>4:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()

import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.fa', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ouFile.write('>' + fields[0] +'\n')
    ouFile.write(fields[9] + '\n')
inFile.close()
ouFile.close()


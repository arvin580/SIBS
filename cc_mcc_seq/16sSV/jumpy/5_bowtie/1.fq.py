import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1].split('fa')[0]+'fq', 'w')
for line in inFile:
    line = line.strip()
    if line.find('>')==0:
        head = line.strip('>')
    else:
        ouFile.write('@' + head + '\n')
        ouFile.write(line + '\n')
        ouFile.write('+\n')
        ouFile.write('h'*len(line)+'\n')
inFile.close()
ouFile.close()

import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.fq', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[5] =='*':
        ouFile.write('@'+fields[0]+'\n')
        ouFile.write(fields[9]+'\n')
        ouFile.write('+'+'\n')
    #ouFile.write(fields[10]+'\n')
        ouFile.write('h'*len(fields[9])+'\n')
inFile.close()
ouFile.close()


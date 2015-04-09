import sys
ouFile = open('duppy.split.seq', 'w')
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        if line.find('chr')!=-1:
            fields = line.split(':')
            ouFile.write(inF.split('.')[0]+'\t'+fields[1]+'\t'+fields[2]+'\n')
            ouFile.write(inF.split('.')[0]+'\t'+fields[1]+'\t'+fields[3]+'\n')

    inFile.close()
ouFile.close()

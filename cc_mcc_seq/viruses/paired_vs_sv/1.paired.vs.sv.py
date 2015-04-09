import sys
ouFile = open('viruses.paired.seq', 'w')
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        if line.find('chr')!=-1:
            fields = line.split('\t')
            ouFile.write(inF.split('.')[0]+'\t'+fields[2]+'\t'+fields[3]+'\n')

    inFile.close()
ouFile.close()

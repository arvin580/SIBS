import sys
ouFile = open('jumpy.paired.seq', 'w')
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        if line.find('chr')!=-1:
            fields = line.split('\t')
            ouFile.write(inF.split('.')[0]+'\t'+fields[1]+'\t'+fields[8]+'\n')

    inFile.close()
ouFile.close()

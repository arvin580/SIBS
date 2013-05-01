def mk_bed(inF):
    inFile = open(inF)
    ouFile = open(inF+'.bed','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
    inFile.close()
    ouFile.close()

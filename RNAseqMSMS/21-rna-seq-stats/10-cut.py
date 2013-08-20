def cut(inF):
    inFile = open(inF)
    ouFile = open(inF+'.morethan2','w')
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        if int(fields[2]) > 2:
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

cut('split-mapped-deletion.normal.seq.filtered.num.mc.gene')

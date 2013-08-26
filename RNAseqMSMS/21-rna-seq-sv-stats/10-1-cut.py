def cut(inF):
    inFile = open(inF)
    ouFile = open(inF+'.more_than_two','w')
    for line in inFile:
        line = line.rstrip()
        fields = line.split('\t')
        if int(fields[2]) > 2:
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

cut('split-mapped-deletion.normal.seq.filtered.num.gene')
cut('split-mapped-duplication.normal.seq.filtered.num.gene')
cut('split-mapped-inversion.normal.seq.filtered.num.gene')
cut('split-mapped-translocation.normal.seq.filtered.num.gene')

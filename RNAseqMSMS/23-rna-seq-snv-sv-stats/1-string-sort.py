D = {}

inFile = open('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_two.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

inFile = open('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_two.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

inFile = open('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_two.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

inFile = open('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_two.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

inFile = open('split-mapped-ion.normal.seq.filtered.num.gene.more_than_two.gene')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D[fields[0]] = 1
inFile.close()

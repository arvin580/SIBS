Name = []
Set = []
def read_data(inF,name):
    Name.append(name)
    L = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(fields[0])
    inFile.close()
    Set.append(set(L))

read_data('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_one.gene','Deletion')
read_data('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_one.gene','Duplication')
read_data('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_one.gene','Inversion')
read_data('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_one.gene','Translocation')

S = Set[0]& Set[1] & Set[2] & Set[3]
for x in S:
    print(x)


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

read_data('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_two.gene','Deletion')
read_data('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_two.gene','Duplication')
read_data('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_two.gene','Inversion')
read_data('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_two.gene','Translocation')

print('### 4 types ###')
S1 = Set[0]& Set[1] & Set[2] & Set[3]
for x in S1:
    print(x)

print('### 3 types ###')
S = Set[0]& Set[1] & Set[2] - S1
for x in S:
    print(x)

S = Set[0]& Set[1]  & Set[3] -S1
for x in S:
    print(x)

S = Set[0] & Set[2] & Set[3] -S1
for x in S:
    print(x)

S =  Set[1] & Set[2] & Set[3] -S1
for x in S:
    print(x)








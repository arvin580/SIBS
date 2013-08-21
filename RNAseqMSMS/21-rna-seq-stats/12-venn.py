def L2c(L):
    return 'c("'+ '","'.join(L) + '")'

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
    Set.append(L)

read_data('split-mapped-deletion.normal.seq.filtered.num.gene.more_than_one.gene','Deletion')
read_data('split-mapped-duplication.normal.seq.filtered.num.gene.more_than_one.gene','Duplication')
read_data('split-mapped-inversion.normal.seq.filtered.num.gene.more_than_one.gene','Inversion')
read_data('split-mapped-translocation.normal.seq.filtered.num.gene.more_than_one.gene','Translocation')


Rcode=r'''
library('Vennerable');
L = list("%s"=%s, "%s"=%s, "%s"=%s, "%s"=%s);
V = Venn(L);
plot(V,doWeights = FALSE);
dev.off()
'''%(Name[0],L2c(Set[0]),Name[1],L2c(Set[1]),Name[2],L2c(Set[2]),Name[3],L2c(Set[3]))
#
##R=Rscript(Rcode)
print(Rcode)

import sys
def sv(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields= line.split(':')
        D[fields[0]]=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
    ouFile.close()
def sv2(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.gene','w')
    for line in inFile:
        line = line.strip()
        fields= line.split(':')
        D[fields[0]]=1
        D[fields[1]]=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\n')
    ouFile.close()


sv('CHC_20s.delition.gene.reads.formated_rna-seq')
sv('CHC_20s.delition.gene.reads.formated_rna-seq')
sv('CHC_20s.duplication.gene.reads.formated_rna-seq')
sv('CHC_20s.inversion.gene.reads.formated_rna-seq')
sv2('CHC_20s.translocation.gene.reads.formated_rna-seq')
sv('ICC_20s.delition.gene.reads.formated_rna-seq')
sv('ICC_20s.duplication.gene.reads.formated_rna-seq')
sv('ICC_20s.inversion.gene.reads.formated_rna-seq')
sv2('ICC_20s.translocation.gene.reads.formated_rna-seq')
sv('ICC_CHC_20s.delition.gene.reads.formatedrna-seq')
sv('ICC_CHC_20s.duplication.gene.reads.formatedrna-seq')
sv('ICC_CHC_20s.inversion.gene.reads.formatedrna-seq')
sv2('ICC_CHC_20s.translocation.gene.reads.formatedrna-seq')

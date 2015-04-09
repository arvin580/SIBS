D1 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/Both.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D1[fields[2]]=1
inFile.close()

D2 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/ICC_Specific.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2[fields[2]]=1
inFile.close()

D3 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/CHC_Specific.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D3[fields[2]]=1
inFile.close()


def sv(inF):
    inFile = open(inF)
    ouFile1  = open('ICC_'+inF+'_rna-seq','w')
    ouFile2  = open('CHC_'+inF+'_rna-seq','w')
    ouFile3  = open('ICC_CHC_'+inF+'rna-seq','w')
    for line in inFile:
        line = line.strip()
        fields = line.split(':')
        if fields[0] in D1:
            ouFile1.write(line+'\n')
        if fields[0] in D2:
            ouFile2.write(line+'\n')
        if fields[0] in D3:
            ouFile3.write(line+'\n')
    inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()
def sv2(inF):
    inFile = open(inF)
    ouFile1  = open('ICC_'+inF+'_rna-seq','w')
    ouFile2  = open('CHC_'+inF+'_rna-seq','w')
    ouFile3  = open('ICC_CHC_'+inF+'rna-seq','w')
    for line in inFile:
        line = line.strip()
        fields = line.split(':')
        if fields[0] in D1 or fields[1] in D1:
            ouFile1.write(line+'\n')
        if fields[0] in D2 or fields[1] in D2:
            ouFile2.write(line+'\n')
        if fields[0] in D3 or fields[1] in D3:
            ouFile3.write(line+'\n')
    inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

sv('20s.delition.gene.reads.formated')
sv('20s.duplication.gene.reads.formated')
sv('20s.inversion.gene.reads.formated')
sv2('20s.translocation.gene.reads.formated')

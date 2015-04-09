D1 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/Exome_Both.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D1[fields[2]]=1
inFile.close()

D2 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/Exome_ICC_Specific.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2[fields[2]]=1
inFile.close()

D3 = {}
inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/3-20/Exome_CHC_Specific.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D3[fields[2]]=1
inFile.close()


inFile = open('sum_snv16sExome.genome_summary')
ouFile1  = open('ICC_whole_rna-seq','w')
ouFile2  = open('CHC_whole_rna-seq','w')
ouFile3  = open('ICC_whole_CHC_rna-seq','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[1] in D1:
        ouFile1.write(line+'\n')
    if fields[1] in D2:
        ouFile2.write(line+'\n')
    if fields[1] in D3:
        ouFile3.write(line+'\n')
inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()

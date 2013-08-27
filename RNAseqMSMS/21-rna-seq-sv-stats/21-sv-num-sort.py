inFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num')
ouFile = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two-num-sorted','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    num = fields[1]
    inFile2 = open('HeLa-Deletion-Duplication-Inversion-Translocation-Gene-more_than_two')
    for line in inFile2:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == gene:
            ouFile.write(gene + '\t' + num+'\t'+'\t'.join(fields[1:])+'\n')
    inFile2.close()
inFile.close()
ouFile.close()

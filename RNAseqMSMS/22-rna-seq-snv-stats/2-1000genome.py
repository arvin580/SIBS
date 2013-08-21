D = {}
inFile = open('hg19_snp137_1000genome.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[-1]]=1
inFile.close()

inFile = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing-dbsnp')
ouFile1 = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing-dbsnp-1000genome','w')
ouFile2 = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing-dbsnp-non_1000genome','w')
for line in inFile:
    fields = line.split('\t')
    if fields[8] in D:
        ouFile1.write(line)
    else:
        ouFile2.write(line)
inFile.close()
ouFile1.close()
ouFile2.close()

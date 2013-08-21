inFile = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing')
ouFile1 = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing-dbsnp','w')
ouFile2 = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing-non_dbsnp','w')
for line in inFile:
    fields = line.split('\t')
    if fields[8]:
        ouFile1.write(line)
    else:
        ouFile2.write(line)
inFile.close()
ouFile1.close()
ouFile2.close()

inFile = open('sum_snv.exome_summary.indel.overall.filter')
ouFile1 = open('sum_snv.exome_summary.indel.overall.filter-dbsnp','w')
ouFile2 = open('sum_snv.exome_summary.indel.overall.filter-non_dbsnp','w')
for line in inFile:
    fields = line.split('\t')
    if fields[8]:
        ouFile1.write(line)
    else:
        ouFile2.write(line)
inFile.close()
ouFile1.close()
ouFile2.close()

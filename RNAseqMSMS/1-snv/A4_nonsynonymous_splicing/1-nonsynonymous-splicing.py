inFile = open('sum_snv.exome_summary')
ouFile = open('sum_snv.exome_summary.nonsynonymous-splicing','w')
for line in inFile:
    fields = line.split('\t')
    if fields[2] == 'nonsynonymous SNV':
        ouFile.write(line)
inFile.close()
ouFile.close()

inFile = open('sum_snv.exome_summary.overall.filter')
ouFile = open('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing','w')
for line in inFile:
    fields = line.split('\t')
    if fields[2] == 'nonsynonymous SNV':
        ouFile.write(line)
inFile.close()
ouFile.close()

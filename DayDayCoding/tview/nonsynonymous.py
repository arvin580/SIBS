inFile = open('sum_snv16s.exome_summary')
ouFile = open('sum_snv16s.exome_summary.nonsynonymous','w')
for line in inFile:
    fields = line.split('\t')
    if fields[2] == 'nonsynonymous SNV':
        ouFile.write(line)
inFile.close()
ouFile.close()


inFile = open('sum_snp1234.genome_summary_candidate.sorted')
ouFile = open('sum_snp1234.genome_summary_candidate.sorted.filtered','w')

for line in inFile:
    fields = line.split('\t')
    if fields[0].find('intronic')==-1 and fields[0].find('downstream')==-1 and fields[0].find('upstream')==-1:
        ouFile.write(line)

inFile.close()
ouFile.close()

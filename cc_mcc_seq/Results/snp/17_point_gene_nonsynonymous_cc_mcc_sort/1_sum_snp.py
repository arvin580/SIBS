inFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write('\t'.join(fields[0:2])+'\t'+str(sum([int(i) for i in fields[2:12]]))+'\t'+str(sum([int(i) for i in fields[12:]]))+'\t'+'\t'.join(fields[2:])+'\n')


inFile.close()

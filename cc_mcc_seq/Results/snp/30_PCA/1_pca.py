inFile=open('sum_snp.genome_combined.sorted.pass012.new')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.pca','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write('_'.join(fields[21:23]+fields[24:26])+'\t'+'\t'.join(fields[39:])+'\n')

inFile.close()
ouFile.close()

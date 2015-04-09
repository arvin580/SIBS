inFile=open('sum_snp.genome_combined.sorted.pass012.new')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.oncotator','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write('\t'.join(fields[21:26])+'\n')

inFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.oncotator','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write('\t'.join(fields[21:26])+'\n')

inFile.close()

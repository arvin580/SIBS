inFile=open('sum_snp.exome_combined.sorted.pass012.new')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[2]!='synonymous SNV' :
        ouFile.write(line+'\n')


inFile.close()
ouFile.close()

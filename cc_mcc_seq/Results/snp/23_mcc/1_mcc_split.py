inFile=open('sum_snp.exome_combined.sorted.pass012.new')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    su=sum([int(item) for item in fields[-10:]])
    if su >0 :
        ouFile.write(line+'\n')

inFile.close()


inFile=open('sum_snp.genome_combined.sorted.pass012.new')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new_mcc','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    su=sum([int(item) for item in fields[-10:]])
    if su >0 :
        ouFile.write(line+'\n')

inFile.close()

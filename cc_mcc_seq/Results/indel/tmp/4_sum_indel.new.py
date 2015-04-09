inFile=open('sum_indel.exome_combined.sorted.pass012')
ouFile=open('sum_indel.exome_combined.sorted.pass012.new','w')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[28]=='.' and fields[8]=='' :
        ouFile.write(line+'\n')

inFile.close()
ouFile.close()



inFile=open('sum_indel.genome_combined.sorted.pass012')
ouFile=open('sum_indel.genome_combined.sorted.pass012.new','w')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[28]=='.' and fields[8]=='' :
        ouFile.write(line+'\n')

inFile.close()
ouFile.close()

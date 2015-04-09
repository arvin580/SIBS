inFile=open('sum_indel.exome_combined.sorted.pass012')
ouFile=open('sum_indel.exome_combined.sorted.pass012.new','w')
ouFile1=open('sum_indel.exome_combined.sorted.pass012.known','w')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[28]=='.' and fields[8]=='' :
        ouFile.write(line+'\n')
    else :
        ouFile1.write(line+'\n')


inFile.close()
ouFile.close()
ouFile1.close()



inFile=open('sum_indel.genome_combined.sorted.pass012')
ouFile=open('sum_indel.genome_combined.sorted.pass012.new','w')
ouFile1=open('sum_indel.genome_combined.sorted.pass012.known','w')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[28]=='.' and fields[8]=='' :
        ouFile.write(line+'\n')
    else :
        ouFile1.write(line+'\n')

inFile.close()
ouFile.close()
ouFile1.close()

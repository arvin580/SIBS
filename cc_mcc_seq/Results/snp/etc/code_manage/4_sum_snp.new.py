import os

os.chdir('exome')
inFile=open('sum_snp.exome_combined.sorted.pass012')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new','w')
ouFile1=open('sum_snp.exome_combined.sorted.pass012.known','w')


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



os.chdir('../genome')
inFile=open('sum_snp.genome_combined.sorted.pass012')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new','w')
ouFile1=open('sum_snp.genome_combined.sorted.pass012.known','w')


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

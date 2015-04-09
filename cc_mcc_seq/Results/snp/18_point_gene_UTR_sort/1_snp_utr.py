import re
inFile=open('sum_snp.genome_combined.sorted.pass012.new')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    s=re.search(r'^UTR',fields[0])
    if s :
        ouFile.write(line+'\n')

inFile.close()
ouFile.close()


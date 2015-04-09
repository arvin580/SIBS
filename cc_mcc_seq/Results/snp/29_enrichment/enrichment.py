import re
dict1=dict()
inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.unique.sym','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    fds=re.split(r'[,;(]',fields[1])
    dict1.setdefault(fds[0],0)
    dict1[fds[0]]+=1

inFile.close()

for key in dict1 :
    ouFile.write(key+'\n')

ouFile.close()


dict1=dict()
inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.unique.sym','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    fds=re.split(r'[,;(]',fields[1])
    dict1.setdefault(fds[0],0)
    dict1[fds[0]]+=1

inFile.close()

for key in dict1 :
    ouFile.write(key+'\n')

ouFile.close()

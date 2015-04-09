import os

os.chdir('exome')

list1=list()
inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.pointsorted','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    list1.append(fields)

inFile.close()


list1.sort(cmp=lambda x,y:cmp(sum([int(i) for i in x[-20:]]),sum([int(j) for j in y[-20:]])),reverse=True)

for item in list1 :
    ouFile.write('\t'.join(item)+'\n')

ouFile.close()


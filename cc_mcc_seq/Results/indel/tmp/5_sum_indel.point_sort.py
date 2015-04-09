list1=list()
inFile=open('sum_indel.exome_combined.sorted.pass012.new')
ouFile=open('sum_indel.exome_combined.sorted.pass012.new.pointsorted','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    list1.append(fields)

inFile.close()


list1.sort(cmp=lambda x,y:cmp(sum([int(i) for i in x[-20:]]),sum([int(j) for j in y[-20:]])),reverse=True)

for item in list1 :
    ouFile.write('\t'.join(item)+'\n')

ouFile.close()




list1=list()
inFile=open('sum_indel.genome_combined.sorted.pass012.new')
ouFile=open('sum_indel.genome_combined.sorted.pass012.new.pointsorted','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    list1.append(fields)

inFile.close()


list1.sort(cmp=lambda x,y:cmp(sum([int(i) for i in x[-20:]]),sum([int(j) for j in y[-20:]])),reverse=True)

for item in list1 :
    ouFile.write('\t'.join(item)+'\n')

ouFile.close()


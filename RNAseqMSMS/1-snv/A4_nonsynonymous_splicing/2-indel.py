inFile = open('sum_snv.exome_summary.indel')
ouFile = open('sum_snv.exome_summary.indel.type', 'w')
D = {}
for line in inFile:
    fields = line.split('\t')
    D.setdefault(fields[2], 0)
    D[fields[2]]+=1
n = 0
for k in D:
    ouFile.write(k + '\t' +str(D[k])+'\n')
    n+=D[k]
ouFile.write('total' + '\t' +str(n)+'\n')


inFile.close()
ouFile.close()


inFile = open('sum_snv.exome_summary.indel.overall.filter')
ouFile = open('sum_snv.exome_summary.indel.overall.filter.type', 'w')
D = {}
for line in inFile:
    fields = line.split('\t')
    D.setdefault(fields[2], 0)
    D[fields[2]]+=1
n = 0
for k in D:
    ouFile.write(k + '\t' +str(D[k])+'\n')
    n+=D[k]
ouFile.write('total' + '\t' +str(n)+'\n')


inFile.close()
ouFile.close()

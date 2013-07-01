inFile = open('sum_snv.exome_summary')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[2]] = 1
inFile.close()
for k in D:
    print(k)

print('##############')
inFile = open('sum_snv.exome_summary.indel')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[2]] = 1
inFile.close()
for k in D:
    print(k)

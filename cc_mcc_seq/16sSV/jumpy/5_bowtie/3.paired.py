import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.paired', 'w')
D = dict()
chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7',
'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15',
'chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[2] in chs:
        h = ':'.join(fields[0].split(':')[0:7])
        D.setdefault(h, [])
        D[h].append(line)
inFile.close()

for k in D :
    if len(D[k]) == 2:
        for item in D[k]:
            ouFile.write(item + '\n')

ouFile.close()

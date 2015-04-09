
dict1=dict()
inFile=open('sum_snp.exome_combined')
ouFile=open('sum_snp.exome_combined.sorted','w')
head=inFile.readline()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[21],[])
    dict1[fields[21]].append(fields)

inFile.close()

chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22']

for key in chr :
    val=dict1[key]
    val.sort(cmp=lambda x,y:cmp(int(x[22]),int(y[22])))
    for item in val :
        ouFile.write('\t'.join(item)+'\n')
for key in dict1 :
    if key not in chr :
        val=dict1[key]
        val.sort(cmp=lambda x,y:cmp(int(x[22]),int(y[22])))
        for item in val :
            ouFile.write('\t'.join(item)+'\n')


dict1=dict()
inFile=open('sum_snp.genome_combined')
ouFile=open('sum_snp.genome_combined.sorted','w')
head=inFile.readline()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[21],[])
    dict1[fields[21]].append(fields)

inFile.close()

chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22']

for key in chr :
    val=dict1[key]
    val.sort(cmp=lambda x,y:cmp(int(x[22]),int(y[22])))
    for item in val :
        ouFile.write('\t'.join(item)+'\n')
for key in dict1 :
    if key not in chr :
        val=dict1[key]
        val.sort(cmp=lambda x,y:cmp(int(x[22]),int(y[22])))
        for item in val :
            ouFile.write('\t'.join(item)+'\n')

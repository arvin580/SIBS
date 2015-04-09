D = dict()
inFile = open('1.sv.stat.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[1:]:
        ch = item.split(':')[0]
        pos1 = int(item.split(':')[1])
        pos2 = int(item.split(':')[2])
        D.setdefault(ch,[])
        D[ch].append([pos1,pos2])
inFile.close()


inFile = open('/netshare1/home1/people/hansun/Data/dbSNP/hg19_snp135.txt')
ouFile = open('1.sv.stat.gene.dbsnp','w')
for line in inFile:
    fields = line.split('\t')
    ch = fields[1]
    pos1 = int(fields[2])
    pos2 = int(fields[3])
    if ch in D:
        for item in D[ch]:
            if not (pos1>item[1]+500 or pos2<item[0]-500):
                ouFile.write(ch+'\t'+str(item[0])+'\t'+str(item[1])+'\n')
                ouFile.write(line)
inFile.close()
ouFile.close()

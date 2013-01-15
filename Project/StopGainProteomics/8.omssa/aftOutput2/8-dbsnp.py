def dbsnp(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[1]+':'+fields[2]]=1
    inFile.close()
    return D
snp = dbsnp('/netshare1/home1/people/hansun/Data/dbSNP/hg19_snp135.txt')

inFile = open('3-stopgain-protein-unique2-filtered.blated.filtered.snv')
ouFile = open('3-stopgain-protein-unique2-filtered.blated.filtered.snv.dbsnp','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>14:
        for i in range(12,len(fields),7):
            k = fields[i]+':'+fields[i+1]
            if k in snp:
                ouFile.write(line+'\n')
                ouFile.write(snp[k]+'\n')
inFile.close()

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
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[12]+':'+fields[13]
    if k in snp:
        print(line)
inFile.close()

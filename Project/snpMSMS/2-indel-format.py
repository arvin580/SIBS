def cosmic(inF):
    inFile = open(inF)
    ouFile = open(inF+'.formated','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[4] == '.':
            fields[4] = ''
        ouFile.write('\t'.join(fields)+'\n')
    inFile.close()
    ouFile.close()
#cosmic('CosmicCodingMuts_v64_02042013_noLimit-indel')

def dbsnp(inF):
    HG = {}
    inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            HG[line1]=line2
        else:
            break
    inFile.close()

    inFile = open(inF)
    ouFile = open(inF+'.formated','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        atcg = fields[9].split(',')
        if atcg[0]=='-':
            x = HG[fields[1]][int(fields[2])].upper()
            atcg[0]=x
            for i in range(1,len(atcg)-1):
                atcg[i]=x+atcg[i]
        else:
            for i in range(1,len(atcg)):
                if atcg[i]=='-':
                    atcg[i]=''
        fields[9]=','.join(atcg)
        ouFile.write('\t'.join(fields)+'\n')
    inFile.close()
    ouFile.close()

dbsnp('snp137CodingDbSnp-indel')


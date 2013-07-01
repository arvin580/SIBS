def dbsnp():
    inFile = open('snp137CodingDbSnp.txt')
    ouFile1 = open('snp137CodingDbSnp-snp','w')
    ouFile2 = open('snp137CodingDbSnp-indel','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[9].find('-')==-1:
            ouFile1.write(line+'\n')
        else:
            ouFile2.write(line+'\n')
    
    inFile.close()
    ouFile1.close()
    ouFile2.close()

def cosmic():
    inFile = open('CosmicCodingMuts_v64_02042013_noLimit.vcf')
    ouFile1 = open('CosmicCodingMuts_v64_02042013_noLimit-snp','w')
    ouFile2 = open('CosmicCodingMuts_v64_02042013_noLimit-indel','w')
    ATCG = ['A','T','C','G','a','t','c','g']
    for i in range(13):
        inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        fields[0] = 'chr' + fields[0]
        if fields[0] == 'chrMT': 
            fields[0] = 'chrM'
        if fields[3] in ATCG and fields[4] in ATCG:
            ouFile1.write('\t'.join(fields)+'\n')
        else:
            ouFile2.write('\t'.join(fields)+'\n')
    
    inFile.close()
    ouFile1.close()
    ouFile2.close()
cosmic()

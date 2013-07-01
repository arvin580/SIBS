D = {}

def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            if flag:
                D[line2].append(flag+':'+line1)
            else:
                D[line2].append(line1)
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')

#unique('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.not-ref-alt-nonstop-KR','INDEL')
#unique('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.ref-alt-nonsynonymous-nonstop-KR','INDEL')
unique('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.not-ref-alt-nonstop-KR','SNV')
#unique('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.ref-alt-nonsynonymous-nonstop-KR','SNV')
#unique('snp137CodingDbSnp-indel.formated.pep.not-ref-alt-nonstop-KR','INDEL')
#unique('snp137CodingDbSnp-indel.formated.pep.ref-alt-nonsynonymous-nonstop-KR','INDEL')
#unique('snp137CodingDbSnp-snp.pep.not-ref-alt-nonstop-KR','SNV')
#unique('snp137CodingDbSnp-snp.pep.ref-alt-nonsynonymous-nonstop-KR','SNV')


ouFile = open('Homo_sapiens.GRCh37.70.pep.all.fa.fa-CosmicCodingMuts_v64_02042013_noLimit-snp.pep.not-ref-alt-nonstop-KR','w')
for k in D:
    ouFile.write('>'+'|'.join(set(D[k]))+'\n')
    ouFile.write(k+'\n')
    ouFile.write('>REVERSE:'+'|'.join(set(D[k]))+'\n')
    ouFile.write(k[::-1]+'\n')
ouFile.close()



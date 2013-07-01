import re
def KR(inF):
    inFile = open(inF)
    ouFile = open(inF+'-KR','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            s=re.search('[K|R](.*[K|R])',line2)
            if s and len(s.group(1))>=6:
                fields = line1.split(':')
                start = int(fields[6])
                end = int(fields[7])
                st = line2.index(s.group(1))
                ouFile.write(':'.join(fields[0:6])+':'+str(start-st)+':'+str(end-st)+':'+':'.join(fields[8:])+'\n')
                ouFile.write(s.group(1)+'\n')
        else:
            break
    inFile.close()
    ouFile.close()

KR('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.not-ref-alt-nonstop')
KR('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.ref-alt-nonsynonymous-nonstop')
KR('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.not-ref-alt-nonstop')
KR('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.ref-alt-nonsynonymous-nonstop')
KR('snp137CodingDbSnp-indel.formated.pep.not-ref-alt-nonstop')
KR('snp137CodingDbSnp-indel.formated.pep.ref-alt-nonsynonymous-nonstop')
KR('snp137CodingDbSnp-snp.pep.not-ref-alt-nonstop')
KR('snp137CodingDbSnp-snp.pep.ref-alt-nonsynonymous-nonstop')

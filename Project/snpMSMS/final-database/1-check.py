def check(inF):
    inFile = open(inF)
    ouFile = open(inF+'-checked','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            if len(line1)>500:
                fields = line1.split(':')
                ouFile.write(':'.join(fields[0:3])+':...:'+':'.join(fields[4:])+'\n')
                ouFile.write(line2+'\n')
            else:
                ouFile.write(line1+'\n')
                ouFile.write(line2+'\n')
        else:
            break
    inFile.close()

check('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.not-ref-alt-nonstop-KR')
check('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.ref-alt-nonsynonymous-nonstop-KR')

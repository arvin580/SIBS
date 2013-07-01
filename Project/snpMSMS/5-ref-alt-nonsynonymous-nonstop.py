def ref_alt(inF):
    inFile = open(inF)
    ouFile = open(inF+'-nonsynonymous-nonstop','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        line3 = inFile.readline().strip()
        line4 = inFile.readline().strip()
        if line1:
            if line2 != line4:
                seq = line4.split('*')[0]
                if len(seq) >= 6:
                    ouFile.write(line3+'\n')
                    ouFile.write(seq+'\n')
        else:
            break
    inFile.close()

ref_alt('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.ref-alt')
ref_alt('snp137CodingDbSnp-indel.formated.pep.ref-alt')
ref_alt('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.ref-alt')
ref_alt('snp137CodingDbSnp-snp.pep.ref-alt')

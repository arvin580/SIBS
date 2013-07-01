def ref_alt(inF):
    inFile = open(inF)
    ouFile = open(inF+'-nonstop','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            if line2.find('*')==-1:
                ouFile.write(line1+'\n')
                ouFile.write(line2+'\n')
        else:
            break
    inFile.close()

ref_alt('CosmicCodingMuts_v64_02042013_noLimit-indel.formated.pep.not-ref-alt')
ref_alt('snp137CodingDbSnp-indel.formated.pep.not-ref-alt')
ref_alt('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.not-ref-alt')
ref_alt('snp137CodingDbSnp-snp.pep.not-ref-alt')

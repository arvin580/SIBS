def pep(inF,inF2):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        D[line] = 1
    inFile.close()
    inFile = open(inF2)
    ouFile = open(inF2+'.'+inF,'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            if line2 in D:
                ouFile.write(line2+'\t')
                ouFile.write(line1+'\n')
        else:
            break
    
    inFile.close()
    ouFile.close()

pep('HeLa-known-SNV-Virus-SV-0.2013_05_28_14_12_35_qry.peptides-pep.pep','HeLa-SNV-Virus-SV-new.fa')
pep('HeLa-known-SNV-Virus-SV-0.2013_05_28_14_12_35_qry.peptides-pep.pep2','HeLa-SNV-Virus-SV-new.fa')

inFile = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3')
ouFile1 = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind','w')
ouFile2 = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind_ONE_UNIQUE','w')
ouFile3 = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind_ALL_UNIQUE','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[3] == 'NEW':
        if fields[2] == 'pFind-ALL-UNIQUE':
            ouFile3.write(line+'\n')
        if fields[1] == 'pFind-ONE-UNIQUE':
            ouFile2.write(line+'\n')
        if fields[0] == 'pFind':
            ouFile1.write(line+'\n')

inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()

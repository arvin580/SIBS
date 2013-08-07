inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    cleavage = fields[2]
    pep = fields[3]
    if cleavage=='Trypsin':
        if pep[0:-1].find('K')!=-1 or pep[0:-1].find('R')!=-1:
            ouFile.write('miss-cleavage'+'\t'+line+'\n')
        else:
            ouFile.write('no-miss-cleavage'+'\t'+line+'\n')
    elif cleavage == 'LysC':
        if pep[0:-1].find('K')!=-1:
            ouFile.write('miss-cleavage'+'\t'+line+'\n')
        else:
            ouFile.write('no-miss-cleavage'+'\t'+line+'\n')
    elif cleavage == 'GluC':
        if pep[0:-1].find('E')!=-1 or pep[0:-1].find('D')!=-1:
            ouFile.write('miss-cleavage'+'\t'+line+'\n')
        else:
            ouFile.write('no-miss-cleavage'+'\t'+line+'\n')
    elif cleavage == 'Trypsin;LysC':
        if pep[0:-1].find('K')!=-1:
            ouFile.write('miss-cleavage'+'\t'+line+'\n')
        else:
            ouFile.write('no-miss-cleavage'+'\t'+line+'\n')

inFile.close()
ouFile.close()

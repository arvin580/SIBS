inFile = open('evidence.txt')
ouFile1 = open('HeLa-peptide-known','w')
ouFile2 = open('HeLa-peptide-genscan','w')
ouFile3 = open('HeLa-peptide-predicted','w')
ouFile4 = open('HeLa-peptide-snv','w')
ouFile5 = open('HeLa-peptide-indel','w')
ouFile6 = open('HeLa-peptide-virus','w')
ouFile7 = open('HeLa-peptide-sv','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[8].find('known')!=-1:
        ouFile1.write(line+'\n')
    elif fields[8].find('GENSCAN')!=-1:
        ouFile2.write(line+'\n')
        if fields[8].find('')!=-1:
            ouFile3.write(line+'\n')
    elif fields[8].find('SNV')!=-1:
        ouFile4.write(line+'\n')
    elif fields[8].find('INDEL')!=-1:
        ouFile5.write(line+'\n')
    elif fields[8].find('VIRUS')!=-1:
        ouFile6.write(line+'\n')
    elif fields[8].find('SV')!=-1:
        ouFile7.write(line+'\n')
inFile.close()

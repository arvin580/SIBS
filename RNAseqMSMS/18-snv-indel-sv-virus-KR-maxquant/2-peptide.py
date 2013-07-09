inFile = open('evidence-unique')
ouFile1 = open('HeLa-peptide-known','w')
ouFile2 = open('HeLa-peptide-genscan','w')
ouFile3 = open('HeLa-peptide-predicted','w')
ouFile4 = open('HeLa-peptide-snv','w')
ouFile5 = open('HeLa-peptide-indel','w')
ouFile6 = open('HeLa-peptide-virus','w')
ouFile7 = open('HeLa-peptide-sv','w')
ouFile8 = open('HeLa-peptide-reverse-contaminated','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[45] or fields[46]:
        ouFile8.write(line+'\n')
    elif fields[8].find('ENSP')!=-1:
        ouFile1.write(line+'\n')
    elif fields[8].find('GENSCAN')!=-1:
        ouFile2.write(line+'\n')
        if fields[8].find('PREDICT-SPLICING')!=-1:
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
ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()
ouFile5.close()
ouFile6.close()
ouFile7.close()
ouFile8.close()

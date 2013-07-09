inFile = open('evidence-unique')
ouFile1 = open('HeLa-peptide-reverse-contaminated','w')
ouFile2 = open('HeLa-peptide-known','w')
ouFile3 = open('HeLa-peptide-snv-indel-predict-virus-sv','w')



for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[45] or fields[46]:
        ouFile1.write('Trypsin'+'\t'+line+'\n')
    elif fields[8].find('ENSP')!=-1:
        ouFile2.write('Trypsin'+'\t'+line+'\n')
    elif fields[8].find('GENSCAN')!=-1:
        if fields[8].find('PREDICT-SPLICING')!=-1:
            ouFile3.write('Trypsin'+'\t'+'PREDICT-SPLICING'+'\t'+line+'\n')
        else:
            ouFile3.write('Trypsin'+'\t'+'PREDICT'+'\t'+line+'\n')
    elif fields[8].find('SNV')!=-1:
        ouFile3.write('Trypsin'+'\t'+'SNV'+'\t'+line+'\n')
    elif fields[8].find('INDEL')!=-1:
        ouFile3.write('Trypsin'+'\t'+'INDEL'+'\t'+line+'\n')
    elif fields[8].find('VIRUS')!=-1:
        if fields[8].find('HUMAN-VIRUS')!=-1:
            ouFile3.write('Trypsin'+'\t'+'HUMAN-VIRUS'+'\t'+line+'\n')
        else:
            ouFile3.write('Trypsin'+'\t'+'VIRUS'+'\t'+line+'\n')
    elif fields[8].find('SV')!=-1:
        if fields[8].find('Deletion')!=-1:
            ouFile3.write('Trypsin'+'\t'+'SV-DELETION'+'\t'+line+'\n')
        elif fields[8].find('Duplication')!=-1:
            ouFile3.write('Trypsin'+'\t'+'SV-DUPLICATION'+'\t'+line+'\n')
        elif fields[8].find('Inversion')!=-1:
            ouFile3.write('Trypsin'+'\t'+'SV-INVERSION'+'\t'+line+'\n')
        elif fields[8].find('Translocation')!=-1:
            ouFile3.write('Trypsin'+'\t'+'SV-TRANSLOCATION'+'\t'+line+'\n')





inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()

def classification(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'-peptide-known','w')
    ouFile2 = open(inF+'-peptide-genscan','w')
    ouFile3 = open(inF+'-peptide-genscan_splicing','w')
    ouFile4 = open(inF+'-peptide-snv','w')
    ouFile5 = open(inF+'-peptide-indel','w')
    ouFile6 = open(inF+'-peptide-sv','w')
    ouFile7 = open(inF+'-peptide-virus','w')
    ouFile8 = open(inF+'-peptide-reverse-contaminated','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[47] or fields[48]:
            ouFile8.write(line+'\n')
        elif fields[10].find('ENSP')!=-1:
            ouFile1.write(line+'\n')
        elif fields[10].find('GENSCAN')!=-1:
            ouFile2.write(line+'\n')
            if fields[10].find('PREDICT-SPLICING')!=-1:
                ouFile3.write(line+'\n')
        elif fields[10].find('SNV')!=-1:
            ouFile4.write(line+'\n')
        elif fields[10].find('INDEL')!=-1:
            ouFile5.write(line+'\n')
        elif fields[10].find('SV')!=-1:
            ouFile6.write(line+'\n')
        elif fields[10].find('VIRUS')!=-1:
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

classification('HeLa-variant-Trypsin-evidence-unique')
classification('HeLa-variant-LysC-evidence-unique')
classification('HeLa-variant-GluC-evidence-unique')

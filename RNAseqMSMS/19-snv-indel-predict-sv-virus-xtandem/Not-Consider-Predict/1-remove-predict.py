def remove(inF):
    inFile = open(inF)
    ouFile = open(inF+'-not_predict','w')
    for line in inFile:
        fields = line.split('\t')
        if fields[1] != 'PREDICT':
            ouFile.write(line)
    inFile.close()
    ouFile.close()

remove('HeLa-peptide-snv-indel-predict-sv-virus-gluc-pep')
remove('HeLa-peptide-snv-indel-predict-sv-virus-lysc-pep')
remove('HeLa-peptide-snv-indel-predict-sv-virus-trypsin-pep')

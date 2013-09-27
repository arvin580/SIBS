def remove(inF):
    inFile = open(inF)
    ouFile = open(inF+'-not_predict','w')
    for line in inFile:
        fields = line.split('\t')
        if fields[1] != 'PREDICT':
            ouFile.write(line)
    inFile.close()
    ouFile.close()

remove('HeLa-variant-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus')
remove('HeLa-variant-LysC-evidence-unique-peptide-snv-indel-predict-sv-virus')
remove('HeLa-variant-Trypsin-evidence-unique-peptide-snv-indel-predict-sv-virus')

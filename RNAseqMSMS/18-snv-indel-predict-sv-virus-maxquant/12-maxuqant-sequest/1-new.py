def new(inF):    
    inFile = open(inF)
    ouFile = open(inF[0:-4]+'-new','w')
    line = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[4][0:2] != 'sp' and fields[4][0:5] != 'DECOY':
            ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

new('HeLa-Peptide-Predict-Maxquant-Sequest.txt')
new('HeLa-Peptide-Variant-Maxquant-Sequest.txt')

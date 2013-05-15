def cleavage(inF):
    inFile = open(inF)
    ouFile = open(inF+'.full-cleavage','w')
    for line in inFile:
        line =line.strip()
        fields = line.split('\t')
        pre = fields[1].split(':')[-2]
        post = fields[1].split(':')[-1]
        if pre != '[' :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

cleavage('HeLa-SV-Deletion-pep')
cleavage('HeLa-SV-Duplication-pep')
cleavage('HeLa-SV-Inversion-pep')
cleavage('HeLa-SV-Translocation-pep')

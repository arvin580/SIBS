def cleavge(inF):
    inFile = open(inF)
    ouFile = open(inF+'.KR','w')
    ouFile2 = open(inF+'.not-KR','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields)>3:
            fds = fields[3].split(':') 
            if fds[-2]=='[' or (fds[-1] ==']' and fields[0][-1]!='K' and fields[0][-1]!='R'):
                ouFile2.write(line+'\n')
            else:
                ouFile.write(line+'\n')

    inFile.close()
    ouFile.close()
    ouFile2.close()
cleavge('HeLa-SNV-INDEL-ALT-pep.gene')

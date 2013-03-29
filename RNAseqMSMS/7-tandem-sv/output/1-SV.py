import os

files = os.listdir('.')
ouFile = open('Homo_SV','w')
for inF in files:
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        if line.find('SV:')!=-1 and line.find('ENSP')==-1:
            ouFile.write(line+'\n')
    inFile.close()

ouFile.close()


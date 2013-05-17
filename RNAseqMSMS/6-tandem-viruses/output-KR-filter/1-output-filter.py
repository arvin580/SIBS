import os

DIR = '../output-KR'
files = os.listdir(DIR)

ouFile1 = open('HeLa-Human-Viruses','w')
ouFile2 = open('HeLa-Viruses','w')
ouFile3 = open('HeLa-Known-Protein','w')
ouFile4 = open('HeLa-Viruses-REVERSE','w')
for f in files:
    if f[-8:] == '.txt.fdr':
        inFile = open(DIR + '/' + f)
        for line in inFile:
            if line.find('REVERSE')!=-1:
                ouFile4.write(line)
            elif line.find('chromosome') != -1:
                ouFile3.write(line)
            elif line.find('HUMAN-VIRUS')!=-1:
                ouFile1.write(line)
            elif line.find('VIRUS')!=-1:
                ouFile2.write(line)
        inFile.close()

ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()



import os

DIR = '../output2'
files = os.listdir(DIR)

ouFile1 = open('HeLa-SNV-INDEL-REF','w')
ouFile2 = open('HeLa-SNV-INDEL-ALT','w')
ouFile3 = open('HeLa-Known-Protein','w')
ouFile4 = open('HeLa-SNV-INDEL-REVERSE','w')
for f in files:
    if f[-8:] == '.txt.fdr':
        inFile = open(DIR + '/' + f)
        for line in inFile:
            if line.find('REVERSE')!=-1:
                ouFile4.write(line)
            elif line.find('chromosome') != -1:
                ouFile3.write(line)
            elif line.find('ALT')!=-1 and line.find('REF') == -1:
                ouFile2.write(line)
            if line.find('REF')!=-1:
                ouFile1.write(line)
        inFile.close()

ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()


